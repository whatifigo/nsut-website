from flask_assets import Bundle

bundles={
        'template_css':Bundle(
        'css/bootstrap.min.css',
        #'lib/font-awesome/css/font-awesome.min.css',
      	'css/screen2.css',
      	'css/header_blue.css',
      	'css/styles_blue.css',
      	output='generated/template_css.css',
        filters='cssmin'
      	
      	),
        'template_js':Bundle(
        'js/jquery-1.11.1.min.js',
        'js/bootstrap.min.js',
        'js/back-to-top.js',
        'js/modernizr.js',
        'js/header.js',
        'lib/jquery.hoverIntent.minified.js',
        output='generated/template_js.js',
        filters='jsmin'
        ),

        'index_css':Bundle(
		'lib/index_new/css.css',
        'lib/index_new/styles_blue.css',
        'lib/index_new/flexslider.css',
		'lib/index_new/scroll.css',
        output='generated/index_css.css',
        filters='cssmin'
        
        ),

        'index_js':Bundle(
          'lib/index_new/jquery.flexslider.js',
          'lib/index_new/main.js',
		  'lib/index_new/jqueryscroller.js',
          output='generated/index_js.js',
          filters='jsmin'
          
          )

}
