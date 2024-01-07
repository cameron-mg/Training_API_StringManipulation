This API is developed to calculate metrics based on string lengths within a text file.

To use the api follow these steps:

1: Clone the repository from GitHub.
2: Add any files you would like the API to act on into the '/test_files' folder.

3: Open a terminal in the same directory as the Dockerfile.
**Please make sure some instance of Docker, e.g., Docker Desktop is running before doing the following.
4: Run the following command: 'docker build -t dominimage .'
5: Run the following command: 'docker run -d --name apicontainer -p 80:80 dominimage'

6: Open powershell and run this command: 'docker exec -it apicontainer bash'
**You are now inside the running container on the powershell window and can run 2 different scripts.

8: Running 'python testcache.py' will loop through each file in '/test_files' and show the difference in execution time between cached and uncached.
9: Running 'python runapi.py' will ask you to type the name of a file in '/test_files'. This returns info in the format specified on the task spec.
**Alternatively the API can be used by opening 127.0.0.1/docs in a web browser after the container is running, this can select files outside of '/test_files'