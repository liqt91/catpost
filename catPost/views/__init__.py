from catPost.views.base import base
from catPost.views.index import index
from catPost.views.user import user

views = (
    (index, '/'),
    (base, '/base'),
    (user,'/user'),
)