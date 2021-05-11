<!DOCTYPE html>
<title>
View Customers
</title> 
    <?php
        include_once('adminHead.php');
    ?>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
    <link rel = "stylesheet" href = "<?php echo base_url('assets/css/viewPreviousOrders.css')?>">
    <br>
        <div class = "table-div">
        <form method = "POST" action = "<?php echo site_url('admin/editOrder');?>">
          <table class = "table">
            <thead>
                <tr>
                    <th>Company Name</th>
                    <th>Contact Person</th>
                    <th>Address</th>
                    <th>Email</th>
                    <th>Phone</th>
                </tr>
            </thead>
            <tbody>
                <?php if($h->num_rows() > 0){ foreach($h->result() as $row){ ?>
                <tr rowspan = "1">
                    <?php if($row->user_name != 'admin'){ ?>
                    <td colspan = "1"><?php echo $row->company_name; ?></td>
                    <td colspan = "1"><?php echo $row->contact_person; ?></td>
                    <td colspan = "1"><?php echo $row->address; ?></td>
                    <td colspan = "1"><?php echo $row->email; ?></td>
                    <td colspan = "1"><?php echo $row->phone; ?></td>
                    <td>
                        <a href="<?php echo site_url('admin/removeCustomer/'.$row->client_num);?>" > Remove Customer </a>
                    </td>
                </tr>
                <?php } } }else{ ?>
                <tr><td>No order(s) found...</td></tr>
                <?php } ?>
            </tbody>
        </table>
        </form>
    </div>
    </body>
</html>