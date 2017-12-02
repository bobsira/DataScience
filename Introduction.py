
# coding: utf-8

# In[1]:

# a list of users, each represented by a dict that contains for each user his or her 
# id(which is a number) and name 
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi"},
    { "id": 4, "name": "Thor"},
    { "id": 5, "name": "Clive"},
    { "id": 6, "name": "Hicks"},
    { "id": 7, "name": "Devin"},
    { "id": 8, "name": "Kate"},
    { "id": 9, "name": "Klein"}
]


# In[2]:

users


# In[3]:

# friendship data, represented as a list of pairs of 
friendships = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),
               (4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]


# In[4]:

friendships


# In[5]:

#to add a list of friends to each user
#first we set each user's friends property to an empty list
for user in users:
    user["friends"] = []


# In[6]:

users


# In[7]:

# then we populate the lists using the friendships data:
for i, j in friendships:
    #this works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j]) #add i as a friend of j
    users[j]["friends"].append(users[i]) #add j as a friend of i


# In[8]:

users
#each user dict now contains a list of friends


# In[9]:

#task one: what's the average number of connections


# In[10]:

#first we find the total number of connections,
#by summing up the lengths of all the friends lists
def number_of_friends(user):
    """how many friends does _user_have?"""
    return len(user["friends"])                 
# length of friends_ids list


# In[11]:

total_connections = sum(number_of_friends(user)
                        for user in users)
# 24


# In[12]:

total_connections


# In[13]:

# and then we just divide by the number of users:
from __future__ import division                  # integer division is lame
num_users = len(users)                           # length of the users list
avg_connections = total_connections / num_users  # 2.4


# In[14]:

avg_connections


# In[15]:

# task two: find the most connected people-the people who have the largest number of friends


# In[16]:

#since there aren't very many users, we can sort them from "most friends" to "least friends"

# create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]


# In[17]:

num_friends_by_id


# In[18]:

sorted(num_friends_by_id,                            # get it sorted
      key=lambda(user_id,num_friends): num_friends,  # by num_friends
      reverse=True)                                  # largest to smallest


# In[19]:

#friends of friends
def friends_of_friend_ids_bad(user):
    # "foaf" is short for "friend of a friend"
    return [foaf["id"]
           for friend in user["friends"]    # for each of user's friends
           for foaf in friend["friends"]]   # get each of _thier_friends


# In[20]:

friends_of_friend_ids_bad(users[0])


# In[23]:

print([friend["id"] for friend in users[0]["friends"]]) #[1,2]


# In[24]:

print( [friend["id"] for friend in users[1]["friends"]] ) #[0,2,3]


# In[25]:

print( [friend["id"] for friend in users[2]["friends"]] ) #[0,1,3]


# In[26]:

#count of mutual friends
from collections import Counter 


# In[27]:

def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]


# In[28]:

def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"]
    that is, if he's not_the_same as all the people in user["friends"]"""
    return all(not_the_same(friend, other_user)
              for friend in user["friends"])


# In[29]:

def friends_of_friends_ids(user):
    return Counter(foaf["id"]
                  for friend in user["friends"]  #for each of my friends
                  for foaf in friend["friends"]  #count *their* friends
                  if not_the_same(user, foaf)    #who aren't mine
                  and not_friends(user, foaf))   #and aren't my friends


# In[30]:

print( friends_of_friends_ids(users[3]) )        # Counter({0: 2, 5:1})


# In[31]:

#list of pairs (user_id, interest)
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


# In[32]:

interests


# In[33]:

#function that finds users with a certain interest
def data_scientists_who_like(target_interest):
    return [user_id
           for user_id, user_interest in interests
           if user_interest == target_interest]


# In[34]:

#building an index from interests to users:


# In[35]:

from collections import defaultdict


# In[37]:

#keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)


# In[38]:

# and another from users to interests:
# keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)


# In[39]:

#to find who has the most interest in common with a given user:
#1.Iterate over the user's interest.
#2.For each interest, iterate over the other users with that interest
#3.Keep count of how many times we see each other user.


# In[40]:

def most_common_interests_with(user):
    return Counter(interested_user_id
                  for interest in interests_by_user_id[user["id"]]
                  for interested_user_id in user_ids_by_interest[interest]
                  if interested_user_id != user["id"])


# In[1]:

salaries_and_tenures = [(83000,8.7), (88000,8.1),
                        (48000,0.7), (76000,6),
                        (69000,6.5), (76000,7.5),
                        (60000,2.5), (83000,10),
                        (48000,1.9), (63000,4.2)]


# In[4]:

# keys are years, values are list of salaries for each tenure
from collections import defaultdict
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)


# In[5]:

# keys are years, each value is average salary for that tenure
average_salary_by_tenure = {
    tenure : sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}


# In[8]:

average_salary_by_tenure


# In[7]:

def tenure_bucket(tenure):
    if tenure < 2 :
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


# In[9]:

#keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)


# In[10]:

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)


# In[13]:

#keys are tenure buckets, values are average salary for that bucket
average_salary_by_bucket = {
    tenure_bucket : sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}


# In[14]:

average_salary_by_bucket


# In[ ]:

def make_chart_salaries_by_tenure():
    tenures = [tenure for salary, tenure in salaries_and_tenure]
    salaries= [salary for salary, tenure in salaries_and_tenure]
    plt.scatter(tenures,salaries)
    plt.xlabel("Y")


# In[15]:

def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0 :
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"


# In[16]:

predict_paid_or_unpaid(3)


# In[17]:

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


# In[18]:

interests


# In[20]:

#to find the most popular interests is simply to count the words
from collections import Counter
words_and_counts = Counter(word for user, interest in interests
                          for word in interest.lower().split())


# In[21]:

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word,count)


# In[ ]:



