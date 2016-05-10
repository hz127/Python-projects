# sample txt file:
# Date: Sat, 5 Jan 2008 09:12:18 -0500
# X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
# To: source@collab.sakaiproject.org
# From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008
# Subject: [sakai] svn commit: r39772 - content/branches/sakai_2-5-x/content-impl/impl/src/java/org/sakaiproject/content/impl

# Count the number of messages from each person
name = raw_input("Enter file:")
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        counts[words[1]] = counts.get(words[1], 0) + 1
    else :
        continue
# print out the person who has the most commits.   
lst = list()
for word, count in counts.items():
    lst.append((count, word))
    lst.sort(reverse = True)
    
print lst[0]

# Count the distribution of the hour of the day for each of the messages.
# Build a dictionary count, then sort the dic by keys 
count = dict()
time = list()
for line in handle:
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        time = words[5].split(':')
        count[time[0]] = count.get(time[0],0) + 1

lst = count.keys()
lst.sort()
for key in lst:
    print key, count[key]
