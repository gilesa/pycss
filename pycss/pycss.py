'''
Created on 2013-02-12

@author: giles
'''
import argparse
import os
import cssparse


def ispycss( f ):
    if f.endswith( '.pycss' ):
        return True
    else:
        return False


def main( path ):
    
    files = []
    
    # Check if valid file or directory specified
    if os.path.isfile( path ) and ispycss( path ):
        print "Loading file:", path
        
        files.append( path );
    elif os.path.isdir( path ):
        # Make sure there is a trailing slash
        if not path.endswith( '/' ):
            path = path + '/'
        
        print "Loading directory:", path
        
        # Load all pycss files and prepend the path 
        dirfiles = filter( ispycss, os.listdir( path ) )
        files[:] = [path + f for f in dirfiles]
    else:
        print "Not a valid file or directory."
                
    for f in files:
        pycssfile = open( f, 'r' )
        output = cssparse.parse( pycssfile )        
        cssfile = open( f.replace( '.pycss', '.css' ), 'w' )
        cssfile.write( output.lstrip() )
        cssfile.close()
        pycssfile.close()
        
    if len( files ) == 1:
        msg = "Successfully converted 1 file!"
    else:
        msg = "Successfully converted {0} files!".format( len( files ) )
    print msg
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser( description='Convert pycss files to valid CSS files.' )
    parser.add_argument( 'input', nargs='?', default='.',
                        help='file to convert or directory in which to convert all pycss files (default: the current directory)' )
    args = parser.parse_args()
    
    main( args.input )