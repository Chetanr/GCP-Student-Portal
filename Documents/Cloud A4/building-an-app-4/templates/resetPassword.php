<html>
<title>
Reset Password
</title> 
	<head>	
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
	<body>
		<link rel="stylesheet" href="<?php echo base_url('assets/css/resetPassword.css')?>"/>
		<div id="image">
			<img src="<?= base_url('assets/images/Logo.jpg') ?>" />
		</div>

		<div id="email-body">
			<p>Dear Customer,</p>
			<p>Please click on the below button to reset your password.</p>
			<br />
			<a href="<?php echo site_url('login/setPassword/'."token=".$token);?>">
				Reset Password
			</a>
			<br>
			<br>
			<p> If the link does not work, please copy and paste the below url in your browser.</p>
			<br>
			<p> Please note that the link is valid only for 24 hours.</p>
			<p><?php echo site_url('login/setPassword/token='.$token);?></p>
			<br />
			<br />
			<p>Regards,</p>
			<p>The Yourframer Team</p>
		</div>
	</body>
</html>
