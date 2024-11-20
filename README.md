# ADS-Code-Test-Results
This repository contains the test results of ADS using CodeQL, and some scripts of additional process.

Things contained in:
  - `AirSim`: the test results of AirSim.
  - `Autoware`: the test results of Autoware.
  - `Apollo`: the test results of Apollo.
  - `codeql-suites`: the query suites for C++, Python and JavaScript language.
  - `scripts`: some programs help to extract data.

We use `CodeQL 2.15.1` to get data. Be sure that you have followed the [instructions](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/preparing-your-code-for-codeql-analysis) and every project's documentation if you want to replicate the results.

To view or use `.sarif` files efficiently, you may need to execute scripts in this repository or install `SARIF Viewer` on VS Code.

<section class="section" id="BibTeX">
  <div class="container is-max-desktop content">
    <h2 class="title">BibTeX</h2>
    <pre><code>@misc{CodeqlRes,
      author       = {Wenyuan Cheng and Zengyang Li and Peng Liang and Ran Mo and Hui Liu},
      title        = {ADS-Code-Test-Results},
      month        = {November},
      year         = {2024},
      url          = {https://github.com/Close-Recover/ADS-Code-Test-Results}
}</code></pre>
  </div>
</section>
