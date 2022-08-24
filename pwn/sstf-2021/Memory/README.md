## Solution:
* Create a symbolic link of /prob/flag inside \<cwd\>/data/. (Might require creating the prob folder locally)
* Name of this symlink could be anything say "flag" itself.
* From inside the \<cwd\>/data/ run the command "tar cvfP ../backup.tar *".
* Execute ./memory binary locally, with an option 4 i.e. to generate a backup/hash/base64 by using the tar file generated above.
   (execute() funtion in libcutil (used by backup option) has been changed so that the binary take the backup of tar file that was gnerated at point 3 above)
   (step 3 and 4 is needed so that the binary does not create a folder name "data" inside the already existing "data" folder)
* Copy this base64 code generated using local binary.
* Invoke the binary in server, send option 5 to restore the file.
* Pass size as 13708 and binary data that is copied in step 5 above to get the flag.
