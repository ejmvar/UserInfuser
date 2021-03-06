# Copyright (C) 2013, AppScale
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import datetime
from google.appengine.ext import db
from serverside import constants

class Logs(db.Model):
  event = db.StringProperty(required=True)
  date = db.DateTimeProperty(auto_now_add=True)
  user = db.StringProperty()
  account = db.StringProperty()
  badgeid = db.StringProperty()
  details = db.StringProperty()
  points = db.StringProperty()
  widget = db.StringProperty()
  success = db.StringProperty()
  api = db.StringProperty()
  is_api = db.StringProperty()
  ip = db.StringProperty()
