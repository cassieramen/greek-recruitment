<!DOCTYPE HTML>
<html>
<head>

<!-- CSS -->
<link href="style.css" type="text/css" rel="stylesheet" media="screen" />
<!-- /CSS -->
<title>EECS 349</title>
</head>

<body>

<?php include 'header.php'; ?>
<br>
<div id='content'>
	<p>Our data was collected from Northwestern University's 2013 Formal Sorority Recruitment. Each potential new member 
		voluntarily filled a survey about themselves before recruitment. These surveys were distributed to all twelve
		sorority chapters. Zeta Beta Zeta </p>
	<h2>Mapped Data</h2>
	<p>We used the data available us to extrapolate some other information about potential new members.</p>
	<h4>Income Level</h4>
	<p>We estimated a persons income based on their zip code. We used the Average Aggregate Earnings for 
		Households found in the 2010 United States census. The income is the average earning for a household
		based on 2011, inflation adjusted dollars. The estimation is not perfect. Sources of error include:
		<ul>
			<li>An average is not always an accurate predictor of a persons wealth. Zip codes with large income
				gaps will often have a very median looking income (close to the national, $65,000 average) when
				in reality residents either fall below the poverty line or in the highest tax bracket.</li>
			<li>Average annual income does not take into account amassed wealth. For example, Zip codes with a 
				large number of retirees likely have a low annual income but have a high amount of saved wealth.</li>
		</ul>
	</p>
	<h4>Public Or Private High School</h4>
	<p>We checked the recruit's high schools against a database of all Public Schools from 2011-12, from the National 
		Center For Education Statistics. The database can be found on 
		http://catalog.data.gov/dataset/list-of-public-elementary-and-secondary-schools-1986-present/resource/af1b40ad-784d-413f-807d-5f7cfcac3208 .
		Due to some alternate spellings in the database we used (i.e. Heights was occasionally abbreviated as Hgts), 
		we had to manually go through the high schools not found on the database to double check them. Sources of error were
		minimal since this was a mostly manual process.

		Possible error comes from human error while double checking the high schools.
	</p>

	<h4>Race</h4>
	<p>We inferred a potential new member's ethnicity from surnames. Using the top 100 surnames by race from the 2010 United
		States census we guessed a new members race. To do this we first assumed that everyone was White, based on the fact that
		Northwestern University as a whole is predominantly White. We then checked if your surname was one of the 100 most popular
		Latino or Asian/Pacific Islander in the United States. We filtered out any overly common surnames from
		this list. For example, Thomas is the 87th most popular name for Asian/Pacific Islander Americans but the 14th most popular
		overall. We ommitted Thomas from the list of popular Asian/Pacific Islander surnames assuming that Thomas was a more common
		name overall. To identify Black students we used a seperate process. Since the 100 most popular Black surnames have a 
		considerable amount of overlap with the most popular White surnames, we flagged a potential new member as possibly Black 
		or White. Then, we searched them on Facebook to determine for certain. Sources of error include:

		<ul>
			<li>Mixed race was not considered in our estimation.</li>
			<li>Garcia is the 82nd most popular Asian/Pacific Islander surname. It is the most popular Latino surname. Garcia was
				ommitted from the Asian/Pacific Islander list but these sorts of strange overlaps are not always avoidable. Adopted
				children or later generation children likely don't have surnames that are easy to classify.</li>
			<li>We used the 100 most popular names, more obscure surnames or races without a large collection of data from the census
				were not included in our estimation.</li>
		</ul>
	</p>
</div>

</body>
</html> 