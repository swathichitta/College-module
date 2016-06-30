from openerp.osv import fields, osv
from openerp import api

class students(osv.osv):
	_name="student"
	_description="students details"
	_columns={
	'stud_profile_pic' : fields.binary('Profile Pic'),
	'name':fields.char('Name',size=20,required=True),
	 'age':fields.integer('Age',size=2,required=True),
	 'phone':fields.integer('Phone',size=10,required=True),
	 'address':fields.text('Address',required=True),
	 'branch':fields.char('Branch',size=5,required=True),
	 'year':fields.integer('Year',size=1),

	 'student_id':fields.one2many('lecturer','lecturer_id','lecturer_details'),


	 'date_start':fields.datetime('DateStart',required=True),
     'date_stop':fields.datetime('DateStop',required=True),

     'feereimbrs':fields.boolean('Feereimbrs'),
     'fees':fields.float('Fees')
	}

	@api.onchange("feereimbrs","fees")
	def onchange_fee(self):
		if self.feereimbrs==True:
			self.fees=35000.00
		elif self.feereimbrs==False:
			self.fees=65000.00

students()
