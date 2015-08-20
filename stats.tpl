<!DOCTYPE html>
<html>
<head>
<link href='https://fonts.googleapis.com/css?family=Roboto' rel='stylesheet' type='text/css'>
<style type="text/css">
  html{
    font-family: 'Roboto', sans-serif;
  }
</style>
</head>
<h1>Taskc Stats Demo</h1>
<ul>
  % for item, value in response.iteritems():
    <li>{{item}} -- {{value}}</li>
  % end
</ul>
</html>