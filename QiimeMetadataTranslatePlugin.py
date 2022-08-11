class QiimeMetadataTranslatePlugin:
    def input(self, filename):
        self.infile = open(filename, 'r')

    def run(self):
        pass

    def output(self, filename):
        tsvfile = open(filename+"/metadata.tsv", 'w')
        csvfile = open(filename+"/sample_data.csv", 'w')
        betafile = open(filename+"/sample_data.beta.csv", 'w')

        # First line
        firstline = self.infile.readline()
        firstlinetsv = firstline.replace("#SampleID", "sampleid")
        tsvfile.write(firstlinetsv)

        firstlinecontents = firstline.strip().split('\t')
        csvcontents = []
        betacontents = []
        csvcontents.append("\"\"")
        betacontents.append("\"\"")
        betacontents.append("\"Name\"")
        for i in range(1, len(firstlinecontents)):
            csvcontents.append("\""+firstlinecontents[i]+"\"")
            betacontents.append("\""+firstlinecontents[i]+"\"")
        for j in range(len(csvcontents)):
            csvfile.write(csvcontents[j])
            if (j != len(csvcontents)-1):
                csvfile.write(",")
            else:
                csvfile.write("\n")
        for j in range(len(betacontents)):
            betafile.write(betacontents[j])
            if (j != len(betacontents)-1):
                betafile.write(",")
            else:
                betafile.write("\n")

        
        # Second line
        secondline = self.infile.readline()
        secondlinecontents = secondline.strip().split('\t')

        #firstlinebeta = firstline.replace("\"\",", "\"\",\"Name\",")
        #betadiv.write(firstlinebeta)
        #firstlineqiime = firstline.replace("\"\"", "\"#SampleID\"")
        #firstlineqiime = firstlineqiime.replace(',','\t').replace('\"','')
        #qiime2file.write(firstlineqiime)
        #tsvfile.write(firstlinetsv)


        for line in self.infile:
            # TSV, same
            tsvfile.write(line)

            linecontents = line.strip().split('\t')
            
            for j in range(len(linecontents)):
                if (secondlinecontents[j] == "numeric"):
                    csvfile.write(linecontents[j])
                else:
                    csvfile.write("\""+linecontents[j]+"\"")
                if (j != len(linecontents)-1):
                    csvfile.write(',')
                else:
                    csvfile.write('\n')
                if (j == 0):
                    betafile.write("\""+linecontents[j]+"\",\""+linecontents[j]+"\",")
                else:
                 if (secondlinecontents[j] == "numeric"):
                    betafile.write(linecontents[j])
                 else:
                    betafile.write("\""+linecontents[j]+"\"")
                 if (j != len(linecontents)-1):
                    betafile.write(',')
                 else:
                    betafile.write('\n')

            
