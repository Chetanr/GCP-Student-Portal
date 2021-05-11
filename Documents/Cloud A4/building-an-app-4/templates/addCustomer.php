<html>
<title>
Add Customer
</title> 
    <?php
        include_once('adminHead.php');
    ?>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
   <body>
    <link rel = "stylesheet" href = "<?php echo base_url('assets/css/addCustomer.css')?>">
    <form id="customer-form" action = "<?php echo site_url('admin/addCustomers'); ?>" method = "POST">
        <br>
        <br>
        <br>
        <br>
        <br>
        <div id = "customer-details">
            <div id = "company">
                <label for = "company-name" class = "style-1"><strong>Company Name:</strong></label>
                &nbsp &nbsp<input type = "text" name = "com-name" class = "style-2">
            </div>
            <br>
            <br>
            <div id = "person">
                <label for = "contract-person" class = "style-1" ><strong>Contact Person:</strong></label>
                &nbsp &nbsp<input type = "text" name = "con-person" class = "style-2">
            </div>
            <br>
            <br>
            <div id = "address">
                <label for = "address" class = "style-1"><strong>Address:</strong></label>
                &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp<input type = "text" name = "addr" class = "style-2">
            </div>  
            <br>
            <br>
            <div id = "mail">
                <label for = "email" class = "style-1"><strong>Email:</strong></label>
                &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp <input type = "text" name = "e-mail" class = "style-2">
            </div>  
            <br>
            <br>
            <div id = "ph">
                <label for = "phone" class = "style-1"><strong>Phone:</strong></label>
                &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp <input type = "text" name = "phone-num" class = "style-2">
            </div> 
            <br>
            <br>
            <div id = "username">
                <label for = "user"class = "style-1" ><strong>Username:</strong></label>
                &nbsp &nbsp &nbsp &nbsp &nbsp <input type = "text" name = "user-name" class = "style-2">
            </div> 
            <br>
            <br>
            <div id = "pwd">
                <label for = "password" class = "style-1"><strong>Password:</strong></label>
                &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp<input type = "text" name = "password" class = "style-2">
            </div> 
            <br>
            <br>
            <div>
                <button type = "submit" id = "submit">Add Customer</button>
                <label id = "invalid-label" name = "invalid"><?php echo isset($error) ? $error : ''; ?></label>
            </div> 
        </form>
</body>
</html>
