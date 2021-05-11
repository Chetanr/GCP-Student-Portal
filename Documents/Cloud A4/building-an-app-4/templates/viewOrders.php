<html>
<title>
View Items
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
        <div id = "sort-div">
        <form method = "POST" action = "<?php echo site_url('admin/filterOrders');?>">
            <select name = "sort">
                <option value = "All"> All</option>
                <option value = "RECEIVED"> Received</option>
                <option value = "IN PROGRESS">In Progress</option>
                <option value = "SHIPPED">Order Shipped</option>
                <option value = "CANCELLED">Cancelled</option>
            </select>
            <button type = "submit" id = "submit">Update</button>
        </form>
        </div>
        <div class = "table-div">
        <form method = "POST" action = "<?php echo site_url('admin/editOrder');?>">
          <table class = "table">
            <thead>
                <tr>
                    <th>Order # &nbsp</th>
                    <th>Item # &nbsp</th>
                    <th>Client &nbsp</th>
                    <th>Customer &nbsp</th>
                    <th>Address &nbsp</th>
                    <th>Phone &nbsp</th>
                    <th>Status &nbsp</th>
                    <th>Size &nbsp</th>
                    <th>Order Date &nbsp</th>
                    <th>Order Kind &nbsp</th>
                    <th>Orientation &nbsp</th>
                    <th>Border &nbsp</th>
                    <th>Tracking Number &nbsp</th>
                    <th>Courier Company &nbsp</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <?php if($h->num_rows() > 0){ foreach($h->result() as $row){ ?>
                <tr rowspan = "1">
                    <td colspan = "1"><?php echo $row->order_num; ?>&nbsp</td>
                    <td colspan = "1"><?php echo $row->sub_order_num; ?>&nbsp</td>
                    <td colspan = "1"><?php echo $row->company_name; ?>&nbsp</td>
                    <td colspan = "1"><?php echo $row->customer; ?>&nbsp</td>
                    <td colspan = "1"><?php echo $row->address; ?>&nbsp</td>
                    <td colspan = "1"><?php echo $row->phone; ?>&nbsp</td>
                    <td colspan = "1"><?php echo $row->status; ?>&nbsp</td>
                    <td colspan = "1"><?php echo $row->size; ?>&nbsp</td>
                    <td colspan = "1"><?php echo $row->order_date; ?>&nbsp</td>
                    <td colspan = "1"><?php echo $row->order_kind; ?>&nbsp</td>
                    <td colspan = "1"><?php echo $row->order_type; ?>&nbsp</td>
                    <td colspan = "1"><?php echo $row->order_sub_type; ?>&nbsp</td>
                    <td colspan = "1"><?php echo $row->tracking_num; ?>&nbsp</td>
                    <td colspan = "1"><?php echo $row->courier_company; ?>&nbsp</td>
                    <td>
                        <a href="<?php echo site_url('admin/editOrder/'.$row->sub_order_num);?>" >Edit</a>
                        &nbsp
                        <a href="<?php echo site_url('admin/printOrder/'.$row->sub_order_num);?>" >Print</a>
                    </td>
                </tr>
                <?php } }else{ ?>
                <tr><td>No order(s) found...</td></tr>
                <?php } ?>
            </tbody>
        </table>
        </form>
    </div>
    </body>
</html>
