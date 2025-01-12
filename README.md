- Docker-container always seek for initial database password, while creating another container.
- So Best practice is to drop the existing database volume

PROCESS:
    - docker-compose logs -f web ( 'web' is the name of service , it can be anything like server/host or anything )
    - docker-compose down
    - docker volume ls 
    - docker volume rm <volume name >
    - finally, docker-compose up

    
     