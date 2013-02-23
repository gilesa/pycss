from rules import rules

def parse( f ):
    output = []
    cssvars = {}
    
    for line in f:
        # Save variable definitions
        if line.startswith( '$' ):
            splitline = line.split( ':' )
            
            if len( splitline ) == 2:
                cssvars.update( { splitline[0].strip(): splitline[1].strip()[:-1] } )
        else:
            # Variables
            if '$' in line:
                start = line.find( '$' )
                
                # Find end position
                semicolon = line.find( ';', start )
                space = line.find( ' ', start )
                if space != -1:
                    end = space
                else:
                    end = semicolon
                    
                var = line[start:end]
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