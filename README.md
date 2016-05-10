#Python Language Bindings

This repository is part of the Isilon SDK, which is an evolving package of documents and files. This README describes how to install and configure Python language bindings in order to access the OneFS API on an Isilon cluster from a Python script. You can use the OneFS API to automate the configuration, maintenance, and monitoring of your Isilon cluster.

* For OneFS API reference documents, discussions, and blog posts, refer to the [OneFS SDK Info Hub](https://community.emc.com/docs/DOC-48273).
* To browse the Isilon InsiqhtIQ statistics API, refer to the [Stat Key Browser](https://github.com/isilon/isilon_stat_browser.git) Github repository.

## Requirements
Python 2.7 and later.

##Install the Python language bindings

You can install the isi_sdk_python library from Github using the pip command.

```sh
pip install git+https://github.com/isilon/isilon_sdk_python_8_0.git
```

**Note:** If you do not have pip installed, you can find instructions here: http://docs.python-requests.org/en/master/user/install/

Alternatively, you can clone this Github repository and run the following command to install the isi_sdk_python library from this repository:

```sh
python setup.py install
```

You may need to install the Python [Setuptools](http://pypi.python.org/pypi/setuptools) on your system, if they are not already installed. For instructions, see http://pypi.python.org/pypi/setuptools.

To import the package and use the bindings, add the following line to the top of the Python scripts that you write:

```python
import isi_sdk
```

## Write code with the Python language bindings

After implementing the steps above, you can write code like the following to interact with the OneFS API. This example gets all NFS exports.

```
import isi_sdk
import urllib3
urllib3.disable_warnings()

# configure username and password
isi_sdk.configuration.username = "userid"
isi_sdk.configuration.password = "pwd"
isi_sdk.configuration.verify_ssl = False

# configure host
host = "https://<ip_address>:8080"
apiClient = isi_sdk.ApiClient(host)
protocolsApi = isi_sdk.ProtocolsApi(apiClient)

# get all exports
nfsExports = protocolsApi.list_nfs_exports()
print "NFS Exports:\n" + str(nfsExports)

```

Copyright (c) 2016 EMC Corporation

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

