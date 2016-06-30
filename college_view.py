from openerp.osv import fields, osv

class College(osv.osv):
	_name="college.college"
	_columns={
		"collegeName":fields.char('CollegeName', size=30, required=True),
		"principal":fields.char('Principal', size=30, required=True),
		"address":fields.text('Address', size=50, required=True),
		"location":fields.char('Location', size=20, required=True),
		"state":fields.selection([('telengana','Telengana'),('assom','Assom'),('kerala','Kerala'),('hp','HP'),('punjab','Punjab'),('delhi','Delhi'),('mp','MP'),('andhra pradesh','Andhra pradesh')],"State",required=True),
		"landmarks":fields.boolean('landmarks', size=2),
		"ranking":fields.char('Ranking', size=6, required=True),
		"passPercentage":fields.float('PassPercentage',align='left', size=5, required=True),
		"date":fields.date('Date', size=10, required=True),
		"openingDate":fields.datetime('OpeningDate',size=20, required=True),
		"academicFee":fields.integer('AcademicFee',size=10, required=True),
		'lecturersid':fields.one2many('lecturer','lecturer_id','Lecturersid')



		
		}
College()
