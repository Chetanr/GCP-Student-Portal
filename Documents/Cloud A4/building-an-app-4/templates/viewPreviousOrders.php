<!DOCTYPE html>
<title>
View Previous Orders
</title> 
    <?php
        include_once('custHead.php');
    ?>

    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>

    <body>
    <link rel = "stylesheet" href = "<?php echo base_url('assets/css/viewPreviousOrders.css')?>">
    <br>
    <div class = "table-div">
        <table class = "table">
            <thead>
                <tr>
                    <th>Item Number</th>
                    <th>Customer</th>
                    <th>Address</th>
                    <th>Phone</th>
                    <th>Date</th>
                    <th>Status</th>
                    <th>Size</th>
                    <th>Order Kind</th>
                    <th>Orientation</th>
                    <th>Border</th>
                    <th>Tracking Number</th>
                    <th>Courier Company</th>
                </tr>
            </thead>
            <tbody>
                <?php if($h->num_rows() > 0){ foreach($h->result() as $row){ ?>
                <tr rowspan = "1">
                    <td colspan = "1"><?php echo $row->sub_order_num; ?></td>
                    <td colspan = "1"><?php echo $row->customer; ?></td>
                    <td colspan = "1"><?php echo $row->address; ?></td>
                    <td colspan = "1"><?php echo $row->phone; ?></td>
                    <td colspan = "1"><?php echo $row->order_date; ?></td>
                    <td colspan = "1"><?php echo $row->status; ?></td>
                    <td colspan = "1"><?php echo $row->size; ?></td>
                    <td colspan = "1"><?php echo $row->order_kind; ?></td>
                    <td colspan = "1"><?php echo $row->order_type; ?></td>
                    <td colspan = "1"><?php echo $row->order_sub_type; ?></td>
                    <td colspan = "1"><?php echo $row->tracking_num; ?></td>
                    <td colspan = "1"><?php echo $row->courier_company; ?></td>
                </tr>
                <?php } }else{ ?>
                <tr><td>No order(s) found...</td></tr>
                <?php } ?>
            </tbody>
        </table>
    </div>
    </body>
</html>