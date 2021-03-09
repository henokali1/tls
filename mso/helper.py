from .g_drive import *

def g_drive_mso(vals):
	original_template_id = '1zvYdumk8HUHuVa7cHmO2vJKNK9vz6915UPdJoAiOo6k'
	# Copy MSO Template
	new_mso_id = copy_template(original_template_id)
	# Update permission to readable by anyone
	update_permission(new_mso_id)
	# Update MSO template form values
	edit_template(document_id=new_mso_id, vals=vals)
	
	for i in vals:
		print(i, vals[i])
	return new_mso_id
