from openerp.osv import fields, osv

class lecturers(osv.osv):
	_name="lecturer"
	_description="Lecturers Details"
	_columns={ 
	 'name':fields.char('Name',size=20,required=True),
	 'age':fields.integer('Age',size=2,required=True),
	 'phone':fields.integer('Phone',size=10,required=True),
	 'address':fields.text('Address',required=True),
	 'subject':fields.char('Subject',size=20,required=True),

	 'lecturer_id':fields.many2one('college.college','collegename'),
	  }

lecturers()

