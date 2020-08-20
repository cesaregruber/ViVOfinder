#!/usr/bin/python



import optparse



parser = optparse.OptionParser(usage= "python ViVOfinder.py -i path-to-file/InputFile.mpileup -o path-to-file/OutputFile.csv", description="ViVOfinder is a bioinformatic tool designed to extract the occurences of all intrahost single nucleotide variant (iSNV) of a viral sample, from pileup file.")
parser.add_option('-i', dest='in_pileup', help='input file in mpileup format [REQUIRED]')
parser.add_option('-o', dest='out_csv', help='output file in csv format [REQUIRED] ')






args, options = parser.parse_args()

infile = open(args.in_pileup,'r')

outfile = open(args.out_csv,'w')


allelecountKeys=['A', 'C', 'G', 'T', 'N', 'insertions','deletions' ]

outfile.write(','.join(['position', 'Ref/consensus',  'coverage', 'A', 'C', 'G', 'T', 'N', 'insertions','deletions' ]) + '\n' )


for line in infile :
    ls = line.split('\t')
    
    position = ls[1]
    refallele = ls[2]
    coverage = ls[3]
    
    string = ls[4]
    
    

    allelecount = {}
    
    allelecount['A'] = 0
    allelecount['C'] = 0
    allelecount['G'] = 0
    allelecount['T'] = 0
    allelecount['N'] = 0
    allelecount['insertions'] = 0
    allelecount['deletions'] = 0

    
    ref = refallele
    
    
    newallele = ""
    indel='false'
    indelcount=0
    indelmax=0
    
    insert = ''
    
    for c in string :
        if c == '+' :
            indel = 'true'
            insert = 'true'
        
        elif c == '-' :
            indel = 'true'
            insert = 'false'

        elif c in ".," and indel=='false' :  # the points stand for forward read, commas stand for reverse read
            allelecount[ref] += 1
        
        elif c in 'AGTCNagtcn' and indel=='false'   :
            newallele = c.upper()
            allelecount[newallele] += 1
        
        elif (c in '0123456789') and (indel == 'true') and (indelcount == 0 ) :
            indelcount = int(c)
            indelmax = indelcount
        
                
        elif c == '*' :
            allelecount['deletions'] += 1
        
        elif (c in '0123456789') and (indel == 'true') and ( indelcount !=0 ) :
            decine = indelcount*10
            indelcount = decine + int(c)
            indelmax = indelcount
        
        elif c in 'ACGTNacgtn' and indel =='true'   :
            indelcount -= 1
            if indelcount == 0 :
                if insert == 'true' :
                    allelecount['insertions'] += indelmax
                elif insert == 'false' :
                    allelecount['deletions'] += indelmax
                else :
                    print 'ERROR at position',  position
                    
                indelmax = 0
                insert = ''
                indel = 'false'
    
    outfile.write(','.join([position, refallele,  coverage]) +'\t' )
    outfile.write(','.join(  [ str(allelecount[c] ) for c in allelecountKeys ] ) +'\n' )

infile.close()
outfile.close()
