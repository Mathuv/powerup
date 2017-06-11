<?php


// Start XML file, create parent node
$doc = new DOMDocument("1.0");
$node = $doc->createElement("workitems");
$parnode = $doc->appendChild($node);

// Opens a connection to a mySQL server
$connection=new mysqli('localhost', 'root', '', 'test');
if (!$connection) {
  die('Not connected : ' . mysql_error());
}


// Select all the rows in the markers table
$query = "SELECT * FROM workitems";
$result = mysqli_query($connection, $query);
if (!$result) {
  die('Invalid query: ' . mysql_error());
}


header("Content-type: text/xml");

//echo 'test2';

// Iterate through the rows, adding XML nodes for each
while ($row = $result->fetch_assoc()){
  // ADD TO XML DOCUMENT NODE
  $node = $doc->createElement("marker");
  $newnode = $parnode->appendChild($node);
  $newnode->setAttribute("name", $row['name']);
  $newnode->setAttribute("address", $row['postcode']);
  $newnode->setAttribute("lat", $row['lat']);
  $newnode->setAttribute("lng", $row['lng']);
  $newnode->setAttribute("workitem", $row['workitem']);
}

echo $doc->saveXML();

?>
