
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
clearInput('#user_login')
fillIn('#user_login', 'Admin')
clearInput('#pass1-text')
fillIn('#pass1-text', 'kaokaokao!1010')
fillIn('#admin_email', 'guidovalle1608@gmail.com')
takeScreenshot()
```


![png](Wordpress_files/Wordpress_3_0.png)


## Fill in the fields


```python
click('#submit')
takeScreenshot()
```


![png](Wordpress_files/Wordpress_5_0.png)


## Congratulations, you have installed Wordpress!

## Now, click on Log In!


```python
click('.button')
fillIn('#user_login', 'Admin')
fillIn('#user_pass', 'kaokaokao!1010')
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
fillIn('#post-title-0', 'My first post!')
highlight('#editor > div > div > div > div.edit-post-header > div.edit-post-header__settings > button.components-button.editor-post-publish-panel__toggle.is-button.is-primary')
takeScreenshot()
click('#editor > div > div > div > div.edit-post-header > div.edit-post-header__settings > button.components-button.editor-post-publish-panel__toggle.is-button.is-primary')
click('#editor > div > div > div > div:nth-child(3) > div > div > div.editor-post-publish-panel__header > div > button')
```


![png](Wordpress_files/Wordpress_13_0.png)


## Now, you can see your post!


```python
takeScreenshot()
clickOnCoveredElement('#editor > div > div > div > div.edit-post-layout__content > div.components-notice-list > div > div > a')
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
takeScreenshot()
clickOnCoveredElement('#submit')

```


![png](Wordpress_files/Wordpress_19_0.png)


## Now, your comment!


```python
takeScreenshot()
```


![png](Wordpress_files/Wordpress_21_0.png)


## Now, lets delete your comment! First, click on edit.


```python
highlight('.comment-edit-link')
takeScreenshot()
click('.comment-edit-link')

```


![png](Wordpress_files/Wordpress_23_0.png)


## Now, click on 'move to Thrash'


```python
highlight('.submitdelete')
takeScreenshot()
click('.submitdelete')

```


![png](Wordpress_files/Wordpress_25_0.png)


## Now, return to the main page. Let's add a new page!


```python
highlight('#wp-admin-bar-site-name > a:nth-child(1)')
takeScreenshot()
click('#wp-admin-bar-site-name > a:nth-child(1)')

```


![png](Wordpress_files/Wordpress_27_0.png)


## Click on 'Pages'


```python
highlight('a.menu-icon-page > div:nth-child(3)')
takeScreenshot()
click('a.menu-icon-page > div:nth-child(3)')
```


![png](Wordpress_files/Wordpress_29_0.png)


## Click on 'Add New'


```python
highlight('.page-title-action')
takeScreenshot()
click('.page-title-action')
```


![png](Wordpress_files/Wordpress_31_0.png)


## Fill the title of your page!


```python
fillIn('#post-title-0', 'New page')
takeScreenshot()
```


![png](Wordpress_files/Wordpress_33_0.png)


## Click on 'publish'


```python
click('#editor > div > div > div > div.edit-post-header > div.edit-post-header__settings > button.components-button.editor-post-publish-panel__toggle.is-button.is-primary')
click('#editor > div > div > div > div:nth-child(3) > div > div > div.editor-post-publish-panel__header > div > button')
```

## Click on 'view page' to view your page!


```python
takeScreenshot()
clickOnCoveredElement('#editor > div > div > div > div.edit-post-layout__content > div.components-notice-list > div > div > a')
```


![png](Wordpress_files/Wordpress_37_0.png)


## Here, your new page! Now, let's change the title of your site! Return to the main page.


```python
highlight('#wp-admin-bar-site-name > a:nth-child(1)')
takeScreenshot()
click('#wp-admin-bar-site-name > a:nth-child(1)')

```


![png](Wordpress_files/Wordpress_39_0.png)


## Click on 'settings'!


```python
highlight('a.menu-icon-settings > div:nth-child(3)')
takeScreenshot()
click('a.menu-icon-settings > div:nth-child(3)')
```


![png](Wordpress_files/Wordpress_41_0.png)


## Now, change the title!


```python
highlight('#blogname')
fillIn('#blogname', ' new name!')
takeScreenshot()
```


![png](Wordpress_files/Wordpress_43_0.png)


## Click on 'Save changes'!


```python
highlight('#submit')
takeScreenshot()
click('#submit')
```


![png](Wordpress_files/Wordpress_45_0.png)


## Now, your site had a new name!


```python
takeScreenshot()
close()
```


![png](Wordpress_files/Wordpress_47_0.png)

