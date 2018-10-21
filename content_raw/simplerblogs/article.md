link:nginx
url:https://nginx.org/
text:nginx

# a simpler way for users to reply to blogs

Commonly, a web server that's hosting  a blog should:

* Present some comments upload form.

* Be able to handle uploaded users _data_ (e.g. post or
  get or whatever requests).
* Then, the web server runs some dynamic code that reads the user
  upload data.
* And then writes/saves something somewhere (e.g. to store the
  end-user's comment). The comment is usually stored in some
  back-end database, like some evil SQL stuff.
* Additionally, the user usually also needs to register an
  account for the blog.

We all know that, right?  In fact, it's so common that most people don't even
realize a sad aspect: all of the points from (1) to (5) are redundant, and we
already have a system for it, that almost everyone uses:  _the email
system_.  It's so obvious that most people are unable to see.  But here is
how:

* Email clients already have highly capable upload forms, with
   capacity of handling attachments, cryptographic signatures,
   etc.
* Email servers already uploaded stuff (texts, attachments).
* Email servers can already run some dynamic code that reads the
   user upload data and reacts accordingly.  Some use this feature
   to dynamically create support tickets from email.
* Email servers can obviously writes/saves something somewhere
   (e.g. to store the end-user's comment).
* The email system allows user registration (e.g. registering to
   free email providers, or registering for a domain name and let
   user host his own mail servers, etc).  The email registration
   is also powerful in that, it already has an infrastructure to
   handle abusers if needed.

So much redundancies.  Since I'll already have an email server, here is how
I'll solve this problem for this blog, in order to less-redundantly allow for
user posts:

* Blog's web server will be a read-only [nginx].  Nothing dynamic, just
   vanilla [nginx].
* Each blog post will have a unique identifier, say, the
   identifier is `123456` for this post.
* The reply link will be a `mailto` anchor
   to the email address `123456.reply@caveman.sexy`.
* The user posts his reply to that email address, and will get to
   set various options by using special tags in the body of the
   email, in order to set his nickname, or whether he wants to be
   notified when someone replies to his comment.
* The mail server will get the message, parse it dynamically, if
   things are OK, then translate it into a HTML/CSS content, and
   update the static pages of this blog.
* Users will then see the updated site html files with the newly
   posted reply.

As a side effect:

* I'll not need to create user registration forms.
* I'll not need to create post-reply forms.
* Since [nginx] will be fully dealing with static content,
  if-modified-since will work conveniently out of the box, and be
  mega fast.

This might not be necessarily new, but it is certainly at least an extremely
uncommon method of handling blog posts/replies.  IMO we live in a very sad time
where most people, even standard bodies, needlessly create redundant systems.
