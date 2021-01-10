## Final Task - Intelligent Security Sistem (CII-4K3)

### Members

- Habib Bahruddin (1301174412)
- Adzkar Fauzie (1301170399)
- Anhar Abimanyu (1301173721)
- Aziz Nurul Iman (1301174667)

### Details

- Feature Processing
  - Subdomain contains bigcompany name ([Top 10 brands phising target](https://www.cybertalk.org/2020/05/04/top-10-brands-phishing-companies/))
    - ex. paypal.com.evil.com
  - Subdomain length (max. 37) ([SEO subdomain length](https://easymysite.com/blogger-limitations/))
  - URL redirection to untrusted site ([CWE-601](https://cwe.mitre.org/data/definitions/601.html))
    - ex. domain.com?goto=evil.com
  - Shortened Links ([Phising using shortened links](https://www.cyren.com/blog/articles/bank-phishing-scam-is-using-shortened-links))
- Classifier
  - [K-Nearest Neighbor](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) (n = 3)
  - [AdaBoost](https://en.wikipedia.org/wiki/AdaBoost) (random_state = 1)
- Datasets
    - https://research.aalto.fi/en/datasets/phishstorm-phishing-legitimate-url-dataset
- Reference
  - https://doi.org/10.1016/j.eswa.2018.09.029
