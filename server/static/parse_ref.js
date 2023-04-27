document.addEventListener("DOMContentLoaded", function () {
  // Find all patterns like [[General solution|general solution]]
  const regex = /\[\[(.+?)\|(.+?)\]\]/g;
  const bodyContent = document.body.innerHTML;

  // Replace each pattern with a link to the article from the database
  const replacedContent = bodyContent.replace(regex, function (match, text, title) {
	//const link = "entry/" + text.replace(/ /g, "_");
    const link = text.replace(/ /g, "_");
	let entry = '<a href="' + window.location.origin + '/entry/'  + link + '">' + title + '</a>'
	//return `<a href="\${link}">\${title}</a>`; // Use backticks (`) instead of single or double quotes
    return entry; // Use backticks (`) instead of single or double quotes
  });

  // Update the body content with the replaced content
  document.body.innerHTML = replacedContent;
});

