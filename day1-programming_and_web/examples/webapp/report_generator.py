import csv
import argparse


def generate_report(number_of_files):

    report_dict = {}

    # For the existing number of files, load it in a global report
    for i in range(1, int(number_of_files) + 1):
        # Here we are generating and string which serves as dictionary key for each file / branch
        branch_number = 'branch' + str(i)
        branch_report = branch_number + '.csv'

        # We are opening the file for reading and 'binary format' which doesn't matter right now
        with open(branch_report, 'rb') as csvfile:
            # We open load the file's content into a python variable using a specific function
            #that understands csv file type.
            report = csv.reader(csvfile, delimiter=';')
            for row in report:
                # Given that report is now a python element containing the csv file information
                #then we can take the values separately, and use it to build a dictionary with
                #with 
                revenue = int(row[2])
                qty = int(row[3])

                # If the product doesn't exist, then we need to create it.
                if row[0] not in products:
                    products[row[0]] = {'qty':qty,'revenue':revenue}
                #    report_dict[row[0]] = products
                # If the product actually exist, then we just need to add the new value
                else:
                    products[row[0]]['qty'] = products[row[0]]['qty'] + qty
                    products[row[0]]['revenue'] = products[row[0]]['revenue'] + revenue
            #report_dict[row[0]] = products
    return products

def convert_to_html(dictionary, indent=0):
    p=[]
    p.append('<ul>\n')
    for k,v in dictionary.iteritems():
        if isinstance(v, dict):
            p.append('<li>'+ str(k) + ':')
            p.append(convert_to_html(v))
            p.append('</li>')
        else:
            p.append('<li>'+ str(k) + ':'+ str(v) + '</li>')
            p.append('</ul>\n')
    return '\n'.join(p)

#def convert_to_html2(dictionary, first_iteration = False):
#    if first_iteration == True:
#        p = []
#        p.append('<html>\n')
#        p.append('<body>\n')

#        if isinstance(v, dict) and k == 'product':
#            p.append('<ul>\n')
#            p.append('<li>'+ str(k) + ':')
#            p.append(convert_to_html(v))
#            p.append('</li>')
#        else:
#            p.append('<li>'+ str(k) + ':'+ str(v) + '</li>')
#            p.append('</ul>\n')


#    p.append('</body>\n')
#    p.append('</html>\n')

    return '\n'.join(p)

if __name__ == '__main__':

    global branches_list
    global branches_dict
    global products

    branches_list = []
    branches_dict = {}
    products = {}

    complete_report = {}

    parser = argparse.ArgumentParser()
    parser.add_argument('num_of_branches', nargs='?', default='3')
    args = parser.parse_args()

#    for branch in range(int(args.num_of_branches)):
    complete_report = generate_report(args.num_of_branches)
    html_dict = convert_to_html(complete_report)
    f = open('index.html', 'w')
    f.write(html_dict)
    print complete_report

