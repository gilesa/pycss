from rules import rules

def parse( f ):
    output = []
    cssvars = {}
    
    for line in f:
        if line.startswith( '$' ):
            splitline = line.split( ':' )
            
            if len( splitline ) == 2:
                cssvars.update( { splitline[0]: splitline[1].strip() } )
        else:
            # Variables
            if '$' in line:
                var = line[line.find( '$' ):line.find( ';' )]
                if var in cssvars:
                    line = line.replace( var, cssvars[var] )
                    
            # Vendor prefixes
            if ':' in line:
                rule = line[:line.find( ':' )].lstrip()
                if rule in rules:                    
                    for prefix in rules[rule]:
                        output.append( line.replace( rule, "".join( [' '] * ( 6 - len( prefix ) ) ) + '-' + prefix + '-' + rule ) )
        
                    line = line.replace( rule, "        " + rule )
            
            
            output.append( line )
        
    return "".join( output )