# pipenv

pipenv is a useful tool for creating virtual environments.
Virtual environments allow you to have libraries and packages on a per-project basis, such that the dependencies of one project don't conflict with those in other projects.
When you initialize a virtual environment, 2 files get created in the root directory of your project. 
You'll see a *Pipfile* and a *Pipfile.lock*. 
The *Pipfile* es the equivalent to a requirements.txt, and it basically just tells us what python packages we're using and what we would need to recreate our environment.
DON'T EVER MANUALLY MODIFY THE **Pipfile.lock*, let pipenv handle that.
The **Pipfile.lock** contains information about the latest stable version of your code. 
If you update any package or library, and it breaks the code, you can always revert back using the Pipfile.lock. 
However, once you've made updates, and are comfortable with the new update libraries and packages, then you can modify the Pipfile.lock file so that it contains the latest information. 

## New Environments
To create a new virtual environment, just `cd` into the folder where you want to create your project, and run:
```commandline
pipenv install
```
To install a new python package, run the same command as above from inside your project's directory, but specifying the packages you wish to install at the end.
Here are a few examples:
```commandline
pipenv install requests          # will install latest available version
pipenv install "requests>=1.4"   # will install a version equal or larger than 1.4.0
pipenv install "requests<=2.13"  # will install a version equal or lower than 2.13.0
pipenv install "requests>2.19"   # will install 2.19.1 but not 2.19.0
```

Once an environment has been created, you can activate it by running:
```commandline
pipenv shell
```
Or to run a command without initiating the full environment, run:
```commandline
pipenv run
```
To deactivate the pipenv environment, you need to run `exit`, not `deactivate`. 
This is because pipenv actually launches a new shell environment.


## Import/Export libraries to/from pipenv projects
If have a pre-existing *requirements.txt* file, and you want to import all those libraries into a pipenv project, run:
```commandline
pipenv install -r /PATH/TO/requirements.txt
```
If you want to export a pipenv's dependecies as a requirements.txt file, you can run the following command to generate the content needed for such a file:
```commandline
pipenv lock -r
```

## Adding packages only for a development environment
To add packages just for a development environment without actually adding the packages to a would be production environment, install the packages with:
```commandline
pipenv install PACKAGE_NAME --dev 
```
  * the `--dev` option adds the packages into a new section within the Pipfile, separate from the main file projects

## Removing/deleting packages from a pipenv 
Pretty straight forward command:
```commandline
pipenv uninstall PACKAGE_NAME
```

## Changing Python version

One way to change your project's python version is to export the dependencies and create a new environment.

Another way to go about this is to first modify the *Pipfile*'s python version to the desired version, and then run the following command to recreate the environment: `pipenv --python PYTHON_VERSION`. 
For example, `pipenv --python 3.5`. 
This removes the old environment and creates a new one

## Deleting a virtual environment
```commandline
pipenv --rm
```

## List path to your virtual environment
```commandline
pipenv --venv
```
^ pipenv actually works more like a wrapper around venv, so you can always go into the path shown by the previous command, and run normal `venv` commands.

## Check for known vulnerabilities
pipenv can actually look at your currently installed packages, and show you if there are known vulnerabilities and if they've been patched in newer versions
```commandline
pipenv check
```

## Updating packages
One way to update packages, is to modify the Pipfile and manually update the corresponding package's version there. 
Then afterwards, just run `pipenv install` and pipenv will detect the change install the corresponding library

## Showing Dependency graphs
```commandline
pipenv graph
```

## Getting ready for production (modifying the Pipfile.lock)
### 1. Update your Pipfile.lock file if necessary, with:
```commandline
pipenv lock
```
^ This will update your Pipfile.lock file with the current libraries in your project.
### 2. Create a virtual environment with the Pipfile.lock
```commandline
pipenv install --ignore-pipfile
```

## Setting environment variables for different projects
To generate environment variables on a per-project basis, you can create a *.env* file in your project's root directory.
Once these environment variables are set, you can access them in python using the *os* module. 