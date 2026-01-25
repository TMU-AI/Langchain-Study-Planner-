Author: Oliver Manuel
Date: 2026-01-06

Description:

    This folder contains configuration files for the Docker image and devcontainer, providing a 
    standardized programming environment that can be modified safely without fear of breaking 
    other environments on the host system. 
    
    These tools are intended to minimize risk of dependency conflicts and broken environments, 
    especially across machines in case of potential collaborations. 

Instructions: 

    devcontainer.json: Controls VS Code's behaviour. 
        Links to the Dockerfile and requirements.txt in the parent directory.
        If you need additional extensions, you can permanently add them here. 

    requirements.txt: Specifies the Python packages to be installed. If you need additional packages, add them here. 

    Dockerfile: Defines the shared container that everyone uses. **Do not edit**.