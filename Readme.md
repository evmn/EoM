# Encyclopedia of Mathematics

As of writing(2023-04-26), there are 9983 entries in [Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Main_Page), 1566 of them redirect to other pages. That is to say, there are 8417 independent entries.

But I can scrape only 8412 of them, when I run the following query, and find the last 5 that failed my constraint.

```sql
select id, name, url from entry where id not in (select eid from latex) and redirect = 0;
```
id|name
:-|:-
592|[Asymptotic expression](https://encyclopediaofmath.org/wiki/Asymptotic_expression)
8202|[Self-intersection, point of](https://encyclopediaofmath.org/wiki/Self-intersection,_point_of)
9092|[Test](https://encyclopediaofmath.org/wiki/Test)
9095|[Testpage](https://encyclopediaofmath.org/wiki/Testpage)
9764|[Weierstrass zeta-function](https://encyclopediaofmath.org/wiki/Weierstrass_zeta-function)


There are 26895 math formulas in **Display Style**, which are enclosed by double dollar. There are several complicated expressions in [Distribution fitting by using the mean of distances of empirical data](https://encyclopediaofmath.org/wiki/Distribution_fitting_by_using_the_mean_of_distances_of_empirical_data).

![](images/Distribution_fitting_by_using_the_mean_of_distances_of_empirical_data/tag12.svg)

The are some errors in the arrays of [Fraser diagram](https://encyclopediaofmath.org/wiki/Fraser_diagram), and I have fixed them.

![](images/Fraser_diagram/array.svg)

## Local Server of EoM

The project has achieved the following goals:

 - List table of contents
 - Browse random entry
 - Search entry title(case insensitive)
 - Display math equation with MathJax

Copy [database](https://t.me/master_thyself/1408) to *db/* folder, run local server with:

```sh
cd server/
python app.py
# or with the following command
#python -m flask run --host=0.0.0.0
```

![](images/server/index.jpg)
![](images/server/ade.jpg)
![](images/server/search_laplace.jpg)

