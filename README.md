pycss
=====

A Python based CSS generator with variables and auto browser-prefixing. It creates a valid CSS file for every pycss file it processes. It can be run on an individual pycss file or a directory where it will process all files with the pycss extension. It can be set to either run once, or to watch the input for changes and automatically update.

Installation
------------

TODO

Syntax
------

pycss follows the same basic syntax as CSS. Variables are denoted using `$`. The browser-prefixing occurs automatically on any CSS rule which requires it.

#### Example pycss input file

	$green: '#00ff00'
	$width: 50%
	
	#example {
		background-color: $green;
		width: $width;
		transform-origin: 10px 10px;
	}
	
	#test {
		color: $green;
		backface-visibility: hidden;
	}

#### Example CSS output file

	#example {
		background-color: '#00ff00';
		width: 50%;
		-webkit-transform-origin: 10px 10px;
		   -moz-transform-origin: 10px 10px;
			-ms-transform-origin: 10px 10px;
			 -o-transform-origin: 10px 10px;
				transform-origin: 10px 10px;
	}
	
	#test {
		color: '#00ff00';
		-webkit-backface-visibility: hidden;
		   -moz-backface-visibility: hidden;
				backface-visibility: hidden;
	}


Running pycss
-------------

pycss.py [-h] [-w] [input]

#### Options

-h : shows help message

-w, --watch : if included, the input is regularly polled for changes and updated

input : the file or directory to parse. Defaults to the current directory.
