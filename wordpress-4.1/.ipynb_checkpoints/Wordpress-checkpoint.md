
## How to install Wordpress


```python
from guide_automator_function import *

get("localhost:8080/")
highlight('#language-continue')
takeScreenshot()

```


![png](Wordpress_files/Wordpress_1_0.png)


## Select your language, and click on the continue button


```python
click('#language-continue')
fillIn('#weblog_title', 'Ubuntu Blog Wordpress')
fillIn('#user_login', 'Admin')
fillIn('#pass1', 'Admin')
fillIn('#pass2', 'Admin')
fillIn('#admin_email', 'guidovalle1608@gmail.com')
takeScreenshot()
```


![png](Wordpress_files/Wordpress_3_0.png)


## Fill in the fields


```python
click('.button')
takeScreenshot()
```


![png](Wordpress_files/Wordpress_5_0.png)


## Congratulations, you have installed Wordpress!

## Now, click on Log In!


```python
click('.button')
fillIn('#user_login', 'Admin')
fillIn('#user_pass', 'Admin')
highlight('#wp-submit')
takeScreenshot()
click('#wp-submit')

```


![png](Wordpress_files/Wordpress_8_0.png)



```python
highlight('#wp-admin-bar-new-content')
takeScreenshot()
```


![png](Wordpress_files/Wordpress_9_0.png)


## It's your admin panel! Click on 'new' to create your first postage!


```python
click('#wp-admin-bar-new-content')
takeScreenshot()
```


![png](Wordpress_files/Wordpress_11_0.png)


## Now, insert your title and click on publish!


```python
fillIn('#title', 'My first post!')
highlight('#publish')
takeScreenshot()
click('#publish')

```


![png](Wordpress_files/Wordpress_13_0.png)


## Now, you can see your post!


```python
highlight('#message > p:nth-child(1) > a:nth-child(1)')
takeScreenshot()
click('#message > p:nth-child(1) > a:nth-child(1)')
```


![png](Wordpress_files/Wordpress_15_0.png)


## Here, your first post! Now, leave a comment


```python
highlight('#comment')
takeScreenshot()
fillIn('#comment', 'Amazing post!')
```


![png](Wordpress_files/Wordpress_17_0.png)


## Tip your comment, and post!


```python
highlight('#submit')
takeScreenshot()
click('#submit')

```


![png](Wordpress_files/Wordpress_19_0.png)


## Now, your comment!


```python
takeScreenshot()
```


![png](Wordpress_files/Wordpress_21_0.png)

