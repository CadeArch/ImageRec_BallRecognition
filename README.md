### TERM PROJECT ROBOT INTELLIGENCE

# MINIMUM PRODUCT (B)
    have robot find ball and push it

# STRETCH GOAL (A)
    push the ball into a region or object (goal)

# EXTRA STRETCH (Beautiful A)
    Identify ball and push it quickly (maybe even in direction it needs to go)
    - maybe teamwork with another robot

    class October 22nd and October 25th
## perception / Cade Ethan -- use any sensor
    1                                             2             3
    where is the cluster of white black pixels / segmentation / algorithm to work simple to complex

    Use sonar sensor to detect object in front of robot - have camera check to see if ball exists in camera range
    if not tell motion planner to continue scanning. if ball is in the camera range segment where ball is in image
    based on segmentation do a hardcoded manuever to re-position robot and check again where ball is in image. If ball
    is in center segment drive to hit the ball.

    save onxx file that is recognizable by all major perception librarys

    Steps simple working model (Get simple working model done by November 12th):
        1 tap into robot API to use Sonar and Camera (start with fixed camera). October 30 ethan
        2 using open CV find model that can detect balls, implementing it as well. October 30 cade
        3 If doesn't exist using pretrained model, train it on images of our ball. November 6 ethan, cade
        4 once we can identify a ball segment that photo. November 12th ethan, cade
        5 based on that segmentation send code back to motion planning to decide on a course to take. november 12 ethan, cade
            5.1 research to find way to know if ball is touching center pixel?

        6 re-evaluate and decide features to build upon to make more efficient and precise



## mobility / Taylor John (perception can help)
## intelligence (integrate every stack) / Brian John Alex
## testing prototyping / Taylor