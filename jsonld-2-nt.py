# =================================================================
#   Transform directory of JSON-LD files into one N-Triples file
#   (files in the directory need to have `.jsonld` extension)
#   arguments:
#   [1] - directory with the json-ld files
#   output:
#   `output_NT_file.nt` - output N-Triples file
# =================================================================
import os
import sys
import rdflib


if(len(sys.argv) < 2):
    print('No json-ld directory is provided, please try again')
    sys.exit()

input_dir = sys.argv[1] + "/"   # directory to list and iterate files
input_file_list = []
output_file = os.getcwd() + "/" + "output_NT_file.nt"

# create the list of only json-ld files in the provided directory to process
for fn in os.listdir(input_dir):
    if fn.endswith(".jsonld"):
        input_file_list.append(input_dir+fn)

print("====================================================================")

nt_graph = rdflib.Graph()    # create an RDF graph to write triples statements to

for f in input_file_list:
    try:
        g = rdflib.Graph()
        g.parse(f, format="json-ld")
        nt_graph += g
        print("Processing json-ld file: ", f)
    except Exception as ex:
        print("Failed to parse json-ld file:", f)
        continue

# serialize the graph as n-triples and save to the output directory
nt_graph.serialize(destination=output_file, format='nt')

print("====================================================================")
print("created the output concatenated N-Triples file: ", output_file)