Melissa using Amazon AWS Polly speech synth
-------

In order to get AWS Polly working you will need to have an AWS account and create some credentials using the AWS credentials

Installing the AWS Cli

(I did mine on a MAC)
https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html

Once installed, you will need to create the configuration files using an aws command.
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

In the cli on Mac you would run:

$ aws configure

Which will create the credentials file after asking you for both your:

aws_access_key
aws_secret_access_key



------------------------------------------------
General Installation after the above is complete
------------------------------------------------

Follow: https://github.com/Melissa-AI/Melissa-Core/wiki/Installation



-------------------
THE ORIGINAL README
-------------------

| |Build Status| |Codacy Badge| |codecov.io|

|

Melissa is a virtual assistant for OS X, Windows and Linux systems. She
currently uses Google Chrome's speech-to-text engine, OS X's ``say``
command, Linux's ``espeak`` command or Ivona TTS along with some magical
scripting which makes her alive, developed by `Tanay
Pant <http://tanaypant.com>`__ and a group of sorcerers. The Web UI for
Melissa has been designed by `Nakul Saxena <http://nakulsaxena.in>`__.

.. raw:: html

   <p align="center">
     <a href="https://www.youtube.com/watch?v=r1yoaq3BcUA"><img src="http://i.imgur.com/OmsI07v.gif"></a>
   </p>

Check out our
`wiki <https://github.com/Melissa-AI/Melissa-Core/wiki>`__, where we
have installation and configuration instructions, usage guide as well as
relevant documentation.

Discussion and Support
~~~~~~~~~~~~~~~~~~~~~~

If you face an issue or require support, please take a look through the
GitHub Issues, as you may find some useful advice there. If you are
still facing issues, feel free to create a post at our `Google Group
Forum <https://groups.google.com/forum/#!forum/melissa-support--discussion-forum/>`__
describing the issue and the steps you have taken to debug it.

Licence
~~~~~~~

`The MIT License
(MIT) <https://github.com/Melissa-AI/Melissa-Core/blob/master/LICENSE.md>`__

.. |Build Status| image:: https://api.travis-ci.org/Melissa-AI/Melissa-Core.svg?branch=master
   :target: https://travis-ci.org/Melissa-AI/Melissa-Core/
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/b1394316e9eb40bbbf51a12530c4f86d
   :target: https://www.codacy.com/app/tanay1337/Melissa-Core?utm_source=github.com&utm_medium=referral&utm_content=Melissa-AI/Melissa-Core&utm_campaign=Badge_Grade
.. |codecov.io| image:: http://codecov.io/github/Melissa-AI/Melissa-Core/coverage.svg?branch=master
   :target: http://codecov.io/github/Melissa-AI/Melissa-Core?branch=master
.. |Join the chat at https://gitter.im/Melissa-AI/Melissa-Core| image:: https://badges.gitter.im/Melissa-AI/Melissa-Core.svg
   :target: https://gitter.im/Melissa-AI/Melissa-Core?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
