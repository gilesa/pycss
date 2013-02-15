pycss
=====

A Python based CSS generator with variables and auto browser-prefixing. It creates a valid CSS file for every pycss file it processes. It can be run on an individual `.pycss` file or a directory where it will process all `.pycss' files.

Installation
------------

TODO

Syntax
------

pycss follows the same basic syntax as css. Variables are denotated using `$`. The browser-prefixing occurs automaticaly on any css rule which requires it.

#### Example pycss file

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

#### Output css file

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

pycss.py [input]

#### Options

input - the file or directory to parse. Defaults to the current directory. 

    