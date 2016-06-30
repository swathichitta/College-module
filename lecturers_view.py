from openerp.osv import fields, osv
from openerp import api

class lecturers(osv.osv):
	
	_name="lecturer"
	_description="Lecturers Details"
	_columns={ 

		'lec_profile_pic' : fields.binary('Profile Pic'),	
		'name':fields.char('Name',size=20,required=True),
		'age':fields.integer('Age',size=2),
		'phone':fields.char('Phone',size=15,required=True),
		'address':fields.text('Address',required=True),
		'subject':fields.char('Subject',size=20,required=True),
		'datestart':fields.datetime('DateStart'),
	    'datestop':fields.datetime('DateStop'),
	    'branch2teach':fields.char('Branch2teach'),
	    'gender':fields.char('Gender',size=7,required=True),
	    'married':fields.char('Married',size=3),

		'lecturer_id':fields.many2one('college.college','Lecturerid'),
		'lect_id':fields.many2many('student','lecturer_id','branch',string='student details')
		

	}
	
	def create(self, cursor, user, vals, context=None):
		vals['phone'] = '+91-'+vals['phone']
		vals['address']=vals['name']+', '+vals['address']

		rec = super(lecturers, self).create(cursor, user, vals, context=context)
		return rec

	@api.onchange("subject","gender","married")
	def onchange_values(self):
		#on change of subject
	    if (self.subject=="dld" or self.subject=="co" or self.subject=="dbms" or self.subject=="aca" or self.subject=="cn"):
	    	self.branch2teach="cse"
	    elif (self.subject=="edc" or self.subject=="bee"):
	    	self.branch2teach="ece"
	    else:
	    	pass
	    #on change of gender and married fields
	    if(self.gender=="male"):
	    	self.name='Mr '+self.name
	    elif self.gender=='female' and self.married=="yes":
	    	self.name='Mrs '+self.name
	    elif self.gender=='female' and self.married=="no":
	    	self.name='Miss '+self.name
	    else:
	    	pass
		
lecturers()





