{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Before your start:\n",
    "- Read the README.md file\n",
    "- Comment as much as you can and use the resources in the README.md file\n",
    "- Happy learning!"
   ]
  },
  {
   "cell_type": "code",
<<<<<<< HEAD
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
=======
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import numpy, pandas and mysqlalchemy (following what you have learned in previous lessons):\n",
    "\n"
>>>>>>> upstream/master
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Challenge 1 - Load and Evaluate the Datasets\n",
    "\n",
    "#### In this challenge we will load two SQL tables from [this link](https://relational.fit.cvut.cz/dataset/Stats). We will then proceed to evaluate the data to see what type of cleaning and manipulation is necessary.\n",
    "\n",
    "In the cell below, create a mysql engine using the link provided above."
   ]
  },
  {
   "cell_type": "code",
<<<<<<< HEAD
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pymysql \n",
    "import sqlalchemy\n",
    "import getpass"
=======
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
>>>>>>> upstream/master
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use this connection to load the `users` table. Load this table into a variable called `users`."
   ]
  },
  {
   "cell_type": "code",
<<<<<<< HEAD
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "conn = pymysql.connect(\n",
    "    host='relational.fit.cvut.cz',\n",
    "    port=3306,\n",
    "    user='guest',\n",
    "    passwd='relational',\n",
    "    db = 'stats')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
=======
   "execution_count": 4,
>>>>>>> upstream/master
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Let's start examining the dataset.\n",
    "\n",
    "First look at the first five rows using the `head` function."
   ]
  },
  {
   "cell_type": "code",
<<<<<<< HEAD
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Tables_in_stats</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>badges</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>comments</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>postHistory</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>postLinks</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>posts</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>tags</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>users</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>votes</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Tables_in_stats\n",
       "0          badges\n",
       "1        comments\n",
       "2     postHistory\n",
       "3       postLinks\n",
       "4           posts\n",
       "5            tags\n",
       "6           users\n",
       "7           votes"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.read_sql(\"SHOW TABLES;\",conn)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Id</th>\n",
       "      <th>Reputation</th>\n",
       "      <th>CreationDate</th>\n",
       "      <th>DisplayName</th>\n",
       "      <th>LastAccessDate</th>\n",
       "      <th>WebsiteUrl</th>\n",
       "      <th>Location</th>\n",
       "      <th>AboutMe</th>\n",
       "      <th>Views</th>\n",
       "      <th>UpVotes</th>\n",
       "      <th>DownVotes</th>\n",
       "      <th>AccountId</th>\n",
       "      <th>Age</th>\n",
       "      <th>ProfileImageUrl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>-1</td>\n",
       "      <td>1</td>\n",
       "      <td>2010-07-19 06:55:26</td>\n",
       "      <td>Community</td>\n",
       "      <td>2010-07-19 06:55:26</td>\n",
       "      <td>http://meta.stackexchange.com/</td>\n",
       "      <td>on the server farm</td>\n",
       "      <td>&lt;p&gt;Hi, I'm not really a person.&lt;/p&gt;\\n\\n&lt;p&gt;I'm ...</td>\n",
       "      <td>0</td>\n",
       "      <td>5007</td>\n",
       "      <td>1920</td>\n",
       "      <td>-1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>101</td>\n",
       "      <td>2010-07-19 14:01:36</td>\n",
       "      <td>Geoff Dalgas</td>\n",
       "      <td>2013-11-12 22:07:23</td>\n",
       "      <td>http://stackoverflow.com</td>\n",
       "      <td>Corvallis, OR</td>\n",
       "      <td>&lt;p&gt;Developer on the StackOverflow team.  Find ...</td>\n",
       "      <td>25</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>37.0</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>101</td>\n",
       "      <td>2010-07-19 15:34:50</td>\n",
       "      <td>Jarrod Dixon</td>\n",
       "      <td>2014-08-08 06:42:58</td>\n",
       "      <td>http://stackoverflow.com</td>\n",
       "      <td>New York, NY</td>\n",
       "      <td>&lt;p&gt;&lt;a href=\"http://blog.stackoverflow.com/2009...</td>\n",
       "      <td>22</td>\n",
       "      <td>19</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>35.0</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>101</td>\n",
       "      <td>2010-07-19 19:03:27</td>\n",
       "      <td>Emmett</td>\n",
       "      <td>2014-01-02 09:31:02</td>\n",
       "      <td>http://minesweeperonline.com</td>\n",
       "      <td>San Francisco, CA</td>\n",
       "      <td>&lt;p&gt;currently at a startup in SF&lt;/p&gt;\\n\\n&lt;p&gt;form...</td>\n",
       "      <td>11</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1998</td>\n",
       "      <td>28.0</td>\n",
       "      <td>http://i.stack.imgur.com/d1oHX.jpg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>6792</td>\n",
       "      <td>2010-07-19 19:03:57</td>\n",
       "      <td>Shane</td>\n",
       "      <td>2014-08-13 00:23:47</td>\n",
       "      <td>http://www.statalgo.com</td>\n",
       "      <td>New York, NY</td>\n",
       "      <td>&lt;p&gt;Quantitative researcher focusing on statist...</td>\n",
       "      <td>1145</td>\n",
       "      <td>662</td>\n",
       "      <td>5</td>\n",
       "      <td>54503</td>\n",
       "      <td>35.0</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Id  Reputation        CreationDate   DisplayName      LastAccessDate  \\\n",
       "0  -1           1 2010-07-19 06:55:26     Community 2010-07-19 06:55:26   \n",
       "1   2         101 2010-07-19 14:01:36  Geoff Dalgas 2013-11-12 22:07:23   \n",
       "2   3         101 2010-07-19 15:34:50  Jarrod Dixon 2014-08-08 06:42:58   \n",
       "3   4         101 2010-07-19 19:03:27        Emmett 2014-01-02 09:31:02   \n",
       "4   5        6792 2010-07-19 19:03:57         Shane 2014-08-13 00:23:47   \n",
       "\n",
       "                       WebsiteUrl            Location  \\\n",
       "0  http://meta.stackexchange.com/  on the server farm   \n",
       "1        http://stackoverflow.com       Corvallis, OR   \n",
       "2        http://stackoverflow.com        New York, NY   \n",
       "3    http://minesweeperonline.com   San Francisco, CA   \n",
       "4         http://www.statalgo.com        New York, NY   \n",
       "\n",
       "                                             AboutMe  Views  UpVotes  \\\n",
       "0  <p>Hi, I'm not really a person.</p>\\n\\n<p>I'm ...      0     5007   \n",
       "1  <p>Developer on the StackOverflow team.  Find ...     25        3   \n",
       "2  <p><a href=\"http://blog.stackoverflow.com/2009...     22       19   \n",
       "3  <p>currently at a startup in SF</p>\\n\\n<p>form...     11        0   \n",
       "4  <p>Quantitative researcher focusing on statist...   1145      662   \n",
       "\n",
       "   DownVotes  AccountId   Age                     ProfileImageUrl  \n",
       "0       1920         -1   NaN                                None  \n",
       "1          0          2  37.0                                None  \n",
       "2          0          3  35.0                                None  \n",
       "3          0       1998  28.0  http://i.stack.imgur.com/d1oHX.jpg  \n",
       "4          5      54503  35.0                                None  "
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "users = pd.read_sql(\"SELECT * FROM users\", conn)\n",
    "users.head(5)"
=======
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
>>>>>>> upstream/master
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, examine the column names and types to see if there is a type mismatch. Use the `dtypes` function."
   ]
  },
  {
   "cell_type": "code",
<<<<<<< HEAD
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "new_col={\"Id\":\"userId\"}\n",
    "users = users.rename(columns=new_col)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>userId</th>\n",
       "      <th>Reputation</th>\n",
       "      <th>CreationDate</th>\n",
       "      <th>DisplayName</th>\n",
       "      <th>LastAccessDate</th>\n",
       "      <th>WebsiteUrl</th>\n",
       "      <th>Location</th>\n",
       "      <th>AboutMe</th>\n",
       "      <th>Views</th>\n",
       "      <th>UpVotes</th>\n",
       "      <th>DownVotes</th>\n",
       "      <th>AccountId</th>\n",
       "      <th>Age</th>\n",
       "      <th>ProfileImageUrl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>-1</td>\n",
       "      <td>1</td>\n",
       "      <td>2010-07-19 06:55:26</td>\n",
       "      <td>Community</td>\n",
       "      <td>2010-07-19 06:55:26</td>\n",
       "      <td>http://meta.stackexchange.com/</td>\n",
       "      <td>on the server farm</td>\n",
       "      <td>&lt;p&gt;Hi, I'm not really a person.&lt;/p&gt;\\n\\n&lt;p&gt;I'm ...</td>\n",
       "      <td>0</td>\n",
       "      <td>5007</td>\n",
       "      <td>1920</td>\n",
       "      <td>-1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>101</td>\n",
       "      <td>2010-07-19 14:01:36</td>\n",
       "      <td>Geoff Dalgas</td>\n",
       "      <td>2013-11-12 22:07:23</td>\n",
       "      <td>http://stackoverflow.com</td>\n",
       "      <td>Corvallis, OR</td>\n",
       "      <td>&lt;p&gt;Developer on the StackOverflow team.  Find ...</td>\n",
       "      <td>25</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>37.0</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>101</td>\n",
       "      <td>2010-07-19 15:34:50</td>\n",
       "      <td>Jarrod Dixon</td>\n",
       "      <td>2014-08-08 06:42:58</td>\n",
       "      <td>http://stackoverflow.com</td>\n",
       "      <td>New York, NY</td>\n",
       "      <td>&lt;p&gt;&lt;a href=\"http://blog.stackoverflow.com/2009...</td>\n",
       "      <td>22</td>\n",
       "      <td>19</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>35.0</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>101</td>\n",
       "      <td>2010-07-19 19:03:27</td>\n",
       "      <td>Emmett</td>\n",
       "      <td>2014-01-02 09:31:02</td>\n",
       "      <td>http://minesweeperonline.com</td>\n",
       "      <td>San Francisco, CA</td>\n",
       "      <td>&lt;p&gt;currently at a startup in SF&lt;/p&gt;\\n\\n&lt;p&gt;form...</td>\n",
       "      <td>11</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1998</td>\n",
       "      <td>28.0</td>\n",
       "      <td>http://i.stack.imgur.com/d1oHX.jpg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>6792</td>\n",
       "      <td>2010-07-19 19:03:57</td>\n",
       "      <td>Shane</td>\n",
       "      <td>2014-08-13 00:23:47</td>\n",
       "      <td>http://www.statalgo.com</td>\n",
       "      <td>New York, NY</td>\n",
       "      <td>&lt;p&gt;Quantitative researcher focusing on statist...</td>\n",
       "      <td>1145</td>\n",
       "      <td>662</td>\n",
       "      <td>5</td>\n",
       "      <td>54503</td>\n",
       "      <td>35.0</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   userId  Reputation        CreationDate   DisplayName      LastAccessDate  \\\n",
       "0      -1           1 2010-07-19 06:55:26     Community 2010-07-19 06:55:26   \n",
       "1       2         101 2010-07-19 14:01:36  Geoff Dalgas 2013-11-12 22:07:23   \n",
       "2       3         101 2010-07-19 15:34:50  Jarrod Dixon 2014-08-08 06:42:58   \n",
       "3       4         101 2010-07-19 19:03:27        Emmett 2014-01-02 09:31:02   \n",
       "4       5        6792 2010-07-19 19:03:57         Shane 2014-08-13 00:23:47   \n",
       "\n",
       "                       WebsiteUrl            Location  \\\n",
       "0  http://meta.stackexchange.com/  on the server farm   \n",
       "1        http://stackoverflow.com       Corvallis, OR   \n",
       "2        http://stackoverflow.com        New York, NY   \n",
       "3    http://minesweeperonline.com   San Francisco, CA   \n",
       "4         http://www.statalgo.com        New York, NY   \n",
       "\n",
       "                                             AboutMe  Views  UpVotes  \\\n",
       "0  <p>Hi, I'm not really a person.</p>\\n\\n<p>I'm ...      0     5007   \n",
       "1  <p>Developer on the StackOverflow team.  Find ...     25        3   \n",
       "2  <p><a href=\"http://blog.stackoverflow.com/2009...     22       19   \n",
       "3  <p>currently at a startup in SF</p>\\n\\n<p>form...     11        0   \n",
       "4  <p>Quantitative researcher focusing on statist...   1145      662   \n",
       "\n",
       "   DownVotes  AccountId   Age                     ProfileImageUrl  \n",
       "0       1920         -1   NaN                                None  \n",
       "1          0          2  37.0                                None  \n",
       "2          0          3  35.0                                None  \n",
       "3          0       1998  28.0  http://i.stack.imgur.com/d1oHX.jpg  \n",
       "4          5      54503  35.0                                None  "
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "users.head()"
=======
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
>>>>>>> upstream/master
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Finally, we'll examine the `describe` function to see the descriptive statistics for the numeric variables. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [],
   "source": [
<<<<<<< HEAD
    "posts = pd.read_sql(\"SELECT * FROM posts\",conn)"
=======
    "# Your code here:\n",
    "\n"
>>>>>>> upstream/master
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Now let's load the posts table in the cell below.\n",
    "\n",
    "Use the same mysql engine to load the posts table into a dataframe called `posts`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
<<<<<<< HEAD
    "posts_col = {'Id':'postId','OwnerUserId':'userId'}\n",
    "posts = posts.rename(columns=posts_col)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>postId</th>\n",
       "      <th>PostTypeId</th>\n",
       "      <th>AcceptedAnswerId</th>\n",
       "      <th>CreaionDate</th>\n",
       "      <th>Score</th>\n",
       "      <th>ViewCount</th>\n",
       "      <th>Body</th>\n",
       "      <th>userId</th>\n",
       "      <th>LasActivityDate</th>\n",
       "      <th>Title</th>\n",
       "      <th>...</th>\n",
       "      <th>AnswerCount</th>\n",
       "      <th>CommentCount</th>\n",
       "      <th>FavoriteCount</th>\n",
       "      <th>LastEditorUserId</th>\n",
       "      <th>LastEditDate</th>\n",
       "      <th>CommunityOwnedDate</th>\n",
       "      <th>ParentId</th>\n",
       "      <th>ClosedDate</th>\n",
       "      <th>OwnerDisplayName</th>\n",
       "      <th>LastEditorDisplayName</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>15.0</td>\n",
       "      <td>2010-07-19 19:12:12</td>\n",
       "      <td>23</td>\n",
       "      <td>1278.0</td>\n",
       "      <td>&lt;p&gt;How should I elicit prior distributions fro...</td>\n",
       "      <td>8.0</td>\n",
       "      <td>2010-09-15 21:08:26</td>\n",
       "      <td>Eliciting priors from experts</td>\n",
       "      <td>...</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1</td>\n",
       "      <td>14.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaT</td>\n",
       "      <td>NaT</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaT</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>59.0</td>\n",
       "      <td>2010-07-19 19:12:57</td>\n",
       "      <td>22</td>\n",
       "      <td>8198.0</td>\n",
       "      <td>&lt;p&gt;In many different statistical methods there...</td>\n",
       "      <td>24.0</td>\n",
       "      <td>2012-11-12 09:21:54</td>\n",
       "      <td>What is normality?</td>\n",
       "      <td>...</td>\n",
       "      <td>7.0</td>\n",
       "      <td>1</td>\n",
       "      <td>8.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>2010-08-07 17:56:44</td>\n",
       "      <td>NaT</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaT</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2010-07-19 19:13:28</td>\n",
       "      <td>54</td>\n",
       "      <td>3613.0</td>\n",
       "      <td>&lt;p&gt;What are some valuable Statistical Analysis...</td>\n",
       "      <td>18.0</td>\n",
       "      <td>2013-05-27 14:48:36</td>\n",
       "      <td>What are some valuable Statistical Analysis op...</td>\n",
       "      <td>...</td>\n",
       "      <td>19.0</td>\n",
       "      <td>4</td>\n",
       "      <td>36.0</td>\n",
       "      <td>183.0</td>\n",
       "      <td>2011-02-12 05:50:03</td>\n",
       "      <td>2010-07-19 19:13:28</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaT</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>135.0</td>\n",
       "      <td>2010-07-19 19:13:31</td>\n",
       "      <td>13</td>\n",
       "      <td>5224.0</td>\n",
       "      <td>&lt;p&gt;I have two groups of data.  Each with a dif...</td>\n",
       "      <td>23.0</td>\n",
       "      <td>2010-09-08 03:00:19</td>\n",
       "      <td>Assessing the significance of differences in d...</td>\n",
       "      <td>...</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2</td>\n",
       "      <td>2.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaT</td>\n",
       "      <td>NaT</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaT</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2010-07-19 19:14:43</td>\n",
       "      <td>81</td>\n",
       "      <td>NaN</td>\n",
       "      <td>&lt;p&gt;The R-project&lt;/p&gt;\\n\\n&lt;p&gt;&lt;a href=\"http://www...</td>\n",
       "      <td>23.0</td>\n",
       "      <td>2010-07-19 19:21:15</td>\n",
       "      <td>None</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>23.0</td>\n",
       "      <td>2010-07-19 19:21:15</td>\n",
       "      <td>2010-07-19 19:14:43</td>\n",
       "      <td>3.0</td>\n",
       "      <td>NaT</td>\n",
       "      <td>None</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   postId  PostTypeId  AcceptedAnswerId         CreaionDate  Score  ViewCount  \\\n",
       "0       1           1              15.0 2010-07-19 19:12:12     23     1278.0   \n",
       "1       2           1              59.0 2010-07-19 19:12:57     22     8198.0   \n",
       "2       3           1               5.0 2010-07-19 19:13:28     54     3613.0   \n",
       "3       4           1             135.0 2010-07-19 19:13:31     13     5224.0   \n",
       "4       5           2               NaN 2010-07-19 19:14:43     81        NaN   \n",
       "\n",
       "                                                Body  userId  \\\n",
       "0  <p>How should I elicit prior distributions fro...     8.0   \n",
       "1  <p>In many different statistical methods there...    24.0   \n",
       "2  <p>What are some valuable Statistical Analysis...    18.0   \n",
       "3  <p>I have two groups of data.  Each with a dif...    23.0   \n",
       "4  <p>The R-project</p>\\n\\n<p><a href=\"http://www...    23.0   \n",
       "\n",
       "      LasActivityDate                                              Title  ...  \\\n",
       "0 2010-09-15 21:08:26                      Eliciting priors from experts  ...   \n",
       "1 2012-11-12 09:21:54                                 What is normality?  ...   \n",
       "2 2013-05-27 14:48:36  What are some valuable Statistical Analysis op...  ...   \n",
       "3 2010-09-08 03:00:19  Assessing the significance of differences in d...  ...   \n",
       "4 2010-07-19 19:21:15                                               None  ...   \n",
       "\n",
       "  AnswerCount  CommentCount  FavoriteCount  LastEditorUserId  \\\n",
       "0         5.0             1           14.0               NaN   \n",
       "1         7.0             1            8.0              88.0   \n",
       "2        19.0             4           36.0             183.0   \n",
       "3         5.0             2            2.0               NaN   \n",
       "4         NaN             3            NaN              23.0   \n",
       "\n",
       "         LastEditDate  CommunityOwnedDate ParentId  ClosedDate  \\\n",
       "0                 NaT                 NaT      NaN         NaT   \n",
       "1 2010-08-07 17:56:44                 NaT      NaN         NaT   \n",
       "2 2011-02-12 05:50:03 2010-07-19 19:13:28      NaN         NaT   \n",
       "3                 NaT                 NaT      NaN         NaT   \n",
       "4 2010-07-19 19:21:15 2010-07-19 19:14:43      3.0         NaT   \n",
       "\n",
       "  OwnerDisplayName LastEditorDisplayName  \n",
       "0             None                  None  \n",
       "1             None                  None  \n",
       "2             None                  None  \n",
       "3             None                  None  \n",
       "4             None                  None  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "posts.head()"
=======
    "# Your code here:\n",
    "\n"
>>>>>>> upstream/master
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Let's repeat what we did with the `users` table and print the first 5 rows, the data types of each column and describe the numeric data.\n",
    "\n",
    "Do this in the following 3 cells below."
   ]
  },
  {
   "cell_type": "code",
<<<<<<< HEAD
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "users_new= users[['userId','Reputation','Views','UpVotes','DownVotes']]"
=======
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
>>>>>>> upstream/master
   ]
  },
  {
   "cell_type": "code",
<<<<<<< HEAD
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>userId</th>\n",
       "      <th>Reputation</th>\n",
       "      <th>Views</th>\n",
       "      <th>UpVotes</th>\n",
       "      <th>DownVotes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>-1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>5007</td>\n",
       "      <td>1920</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>101</td>\n",
       "      <td>25</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>101</td>\n",
       "      <td>22</td>\n",
       "      <td>19</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>101</td>\n",
       "      <td>11</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>6792</td>\n",
       "      <td>1145</td>\n",
       "      <td>662</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   userId  Reputation  Views  UpVotes  DownVotes\n",
       "0      -1           1      0     5007       1920\n",
       "1       2         101     25        3          0\n",
       "2       3         101     22       19          0\n",
       "3       4         101     11        0          0\n",
       "4       5        6792   1145      662          5"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "users_new.head()"
=======
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
>>>>>>> upstream/master
   ]
  },
  {
   "cell_type": "code",
<<<<<<< HEAD
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>postId</th>\n",
       "      <th>Score</th>\n",
       "      <th>userId</th>\n",
       "      <th>ViewCount</th>\n",
       "      <th>CommentCount</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>23</td>\n",
       "      <td>8.0</td>\n",
       "      <td>1278.0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>22</td>\n",
       "      <td>24.0</td>\n",
       "      <td>8198.0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>54</td>\n",
       "      <td>18.0</td>\n",
       "      <td>3613.0</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>13</td>\n",
       "      <td>23.0</td>\n",
       "      <td>5224.0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>81</td>\n",
       "      <td>23.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   postId  Score  userId  ViewCount  CommentCount\n",
       "0       1     23     8.0     1278.0             1\n",
       "1       2     22    24.0     8198.0             1\n",
       "2       3     54    18.0     3613.0             4\n",
       "3       4     13    23.0     5224.0             2\n",
       "4       5     81    23.0        NaN             3"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "posts_new= posts[['postId', 'Score','userId','ViewCount','CommentCount']]\n",
    "posts_new.head()"
=======
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
>>>>>>> upstream/master
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Challenge 2 - Prepare the Datasets for Merging and Merge\n",
    "\n",
    "#### We would like to join a subset of columns from each table. To ease the process, let's create a new dataframe containing a subset of columns for both `posts` and `users`\n",
    "\n",
    "In the cell below, create a new dataframe called `posts_subset` containing only the columns: `Id`, `Score`, `OwnerUserID`, `ViewCount` ,`CommentCount`"
   ]
  },
  {
   "cell_type": "code",
<<<<<<< HEAD
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>userId</th>\n",
       "      <th>Reputation</th>\n",
       "      <th>Views</th>\n",
       "      <th>UpVotes</th>\n",
       "      <th>DownVotes</th>\n",
       "      <th>postId</th>\n",
       "      <th>Score</th>\n",
       "      <th>ViewCount</th>\n",
       "      <th>CommentCount</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>-1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>5007</td>\n",
       "      <td>1920</td>\n",
       "      <td>2175</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>5007</td>\n",
       "      <td>1920</td>\n",
       "      <td>8576</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>-1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>5007</td>\n",
       "      <td>1920</td>\n",
       "      <td>8578</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>-1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>5007</td>\n",
       "      <td>1920</td>\n",
       "      <td>8981</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>-1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>5007</td>\n",
       "      <td>1920</td>\n",
       "      <td>8982</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   userId  Reputation  Views  UpVotes  DownVotes  postId  Score  ViewCount  \\\n",
       "0      -1           1      0     5007       1920    2175      0        NaN   \n",
       "1      -1           1      0     5007       1920    8576      0        NaN   \n",
       "2      -1           1      0     5007       1920    8578      0        NaN   \n",
       "3      -1           1      0     5007       1920    8981      0        NaN   \n",
       "4      -1           1      0     5007       1920    8982      0        NaN   \n",
       "\n",
       "   CommentCount  \n",
       "0             0  \n",
       "1             0  \n",
       "2             0  \n",
       "3             0  \n",
       "4             0  "
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "users_new.merge(posts_new).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "userId        int64\n",
       "Reputation    int64\n",
       "Views         int64\n",
       "UpVotes       int64\n",
       "DownVotes     int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "users_new.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "postId            int64\n",
       "Score             int64\n",
       "userId          float64\n",
       "ViewCount       float64\n",
       "CommentCount      int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "posts_new.dtypes"
=======
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
>>>>>>> upstream/master
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In the cell below, create a dataframe called `users_subset` containing only the columns `Id`, `Reputation`, `Views`, `UpVotes`, `DownVotes`."
   ]
  },
  {
<<<<<<< HEAD
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1, missing userId column from posts"
=======
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
>>>>>>> upstream/master
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### You will note that the Id column does not refer to the same thing in both tables. In the posts table, it refers to the post ID and in the users table it refers to the user ID. \n",
    "\n",
    "In the `users_subset` dataframe, rename the `Id` column to `UserId`. Do this using the option `inplace=True`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In the `posts_subset` dataframe, rename the `Id` column to `PostId`. Do this using the option `inplace=True`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We identify the only column that the two tables have in common as the user ID. However, this column is called `UserId` in the `users_subset` table and `OwnerUserId` in the `posts_subset` table. Using what we have previously learned about merging two dataframes and looking at the documentation [here](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html), merge the two dataframes. Name the merged dataframe `stackoverflow`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Check to see if you have kept both key columns (if you join by making one of the columns an index first, this can be avoided).\n",
    "\n",
    "If both columns are present in `stackoverflow`, drop `OwnerUserId`. Do this using `inplace=True`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Challenge 3 - Cleaning Up the Data\n",
    "\n",
    "Now that we have merged the two dataframes, let's handle the missing values.\n",
    "\n",
    "Find the number of missing values in each column by applying the `isna()` function to the dataframe. Then apply the `sum()` function to that to find the count of missing values in each column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We see that about half of all observations in the view count column are missing. Let's examine these observations and why they have missing data. Create a subset of rows that have a missing value in the `ViewCount`. Look at the `describe()` function for that subset. You output should look like in the table below.\n",
    "\n",
    "![describe table](../describe-table.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It seems that there is a mix of users. They do not have a high comment count but they do have some upvotes and downvotes. Therefore, it would not make sense to fill these values with zero. \n",
    "\n",
    "If we investigate further, we will see that there are some users that have view counts missing for some posts but not others. We will cover different ways of investigating further in future lessons. What we can certainly say is that we should not fill all cells with the same values. One way to fill the values is using linear interpolation. Linear interpolation assumes that there is a line between two points and places all observations between the two points along that line. You can read more about linear interpolation [here](https://en.wikipedia.org/wiki/Linear_interpolation).\n",
    "\n",
    "To apply linear interpolation to our missing data, we use the `interpolate` function in pandas. You can read the documentation for this function [here](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.interpolate.html).\n",
    "\n",
    "Apply the `interpolate` function to the `ViewCount` column. Use `inplace=True`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Bonus Challenge - Fill the Missing Data Using Linear Regression\n",
    "\n",
    "We have learned about linear regression in the prework. To read more about linear regression in Python, click [here](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html).\n",
    "\n",
    "Create a linear model where the Y variable is the `ViewCount` and the X variable is `Score`. Make sure to use only rows that do not contain `NaN` by filtering them out.\n",
    "\n",
    "Use this regression model to produce a fitted value for every `NaN`. Using the `np.where` function, assign the predicted value only to rows where you have a `NaN`.\n",
    "\n",
    "Tip: If you get an error when creating your linear model, reshape the data to the correct shape (a 2D array) by appending `.values.reshape(-1, 1)` to the column. Also, transform the predicted data from a numpy array back to a dataframe and use only one column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We have seen that both `UserId` and `PostsId` are treated as numeric even though they do not describe anything quantitative about the data. We would like to exclude them from any numeric calculations. To do this, we should change them from numeric to string. Transform each column from numeric to string using the `astype` function and pass the argument `'str'` to the function. Since we cannot do this in place, assign these new values back to their original column names. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here:\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### We would like to simplify the comment count variable by bucketing this variable. \n",
    "\n",
    "In the cell below, we have created 5 bins. Bucket this variable into equal width bins using the `cut` function. Create a new column called `CommentBins` and assign the bucketed data to this column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "comment_labels = ['Very Low', 'Low', 'Moderate', 'High', 'Very High']\n",
    "# Your code here:\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
<<<<<<< HEAD
   "version": "3.7.4"
=======
   "version": "3.6.8"
>>>>>>> upstream/master
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
