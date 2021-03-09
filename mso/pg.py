import g_drive as gd

# d=['1-Rodf_MziRZXieJDGp3gdy4E-6883Gc0RzGO8jpDM-8']
# for i in d:
#     gd.delete_drive_file(i)

# gd.copy_file('1zvYdumk8HUHuVa7cHmO2vJKNK9vz6915UPdJoAiOo6k', 'mso_1')
# gd.share_folder('1gu8wLH2uoyCEs4jpg9ZZpyGOc2ypqYTD')
original_template_id = '1zvYdumk8HUHuVa7cHmO2vJKNK9vz6915UPdJoAiOo6k'
gd.copy_template(original_template_id)
all_files = gd.list_files()
print(all_files)
