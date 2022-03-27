
# patent-server
## Index
  - [Overview](#overview) 
  - [Getting Started](#getting-started)
  - [Contributing](#contributing)
  - [Authors](#authors)
  - [License](#license)

## About Repository
<!--Wirte one paragraph of project description -->  
&nbsp;The project implemented a patent big data analysis platform for individual patent applicants.

## Overview
<!-- Write Overview about this project -->
&nbsp; **South of Korea** has the highest patent application rate as a percentage of GDP-population, and the registration rate is still low at **13%**, even though the number of individual applications has increased 6 times compared to 2002.

&nbsp; Most individual applicants are rejected for registration as 'similar patents'. This occurs because the individual did not find similar patents through patent analysis. (Professionalism, time, and labor required for a patent search are all insufficient.)

&nbsp; To solve these difficulties, the project derives a significant search expression using **Word2Vec** and **LDA** techniques. In addition, significant technical taxonomy is extracted through the **LSA** technique.

=> [Project Description and result (detail)](https://star7sss.tistory.com/369) (My Blog)

## Getting Started
**click `Code - Download ZIP` and  unzip it**

### How to run server

1. Before opening the main server, `mongo DB` and `middle server` must be activated.
   <br>install: [Mongo DB](https://www.mongodb.com/), [Middle server](https://github.com/simp7/patent-middle-server)
2. In the terminal, type `python manage.py runserver`.

If you don't have the `Django`, please install it from [this link](https://pypi.org/project/Django/).
or  in the terminal, type `pip  install  django`.

## Contributing
<!-- Write the way to contribute -->
I am looking for someone to help with this project. Please advise and point out.  
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## Authors
  - [jangThang](https://github.com/JangThang) - **Wooyoung Jang** - <star7sss@naver.com>
 
See also the list of [contributors](https://github.com/jangThang/readmeTemplate/contributors) who participated in this project.
<!--
## Used or Referenced Projects
 - [referenced Project](project link) - **LICENSE** - little-bit introduce
-->

## License

```
MIT License

Copyright (c) 2022 jangThang

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
```
