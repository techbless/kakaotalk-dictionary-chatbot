<?php
	include("simple_html_dom.php");
	
	$data = json_decode(file_get_contents('php://input'));
 	$request = $data->content;

	$request = str_replace(' ', '%20', $request);	

 	$html = file_get_html('http://endic.naver.com/search.nhn?sLn=kr&isOnlyViewEE=N&query=' . $request);
	
 	$kind = $html->find('span.fnt_k09', 0)->plaintext;
 	$mean = $html->find('span.fnt_k05', 0)->plaintext;
 	$result = $kind . ' ' . $mean;

	if($result == ' ') {
		echo <<< EOD
		{ 
	  		"message": {
	  		"text": "검색결과를 찾지 못했습니다."
	  		}
		}
EOD;
	} else {
		echo <<< EOD
		{ 
			"message": {
	  		"text": "$result"
	  		}
		}
EOD;
	}

?>
