# A GYP include file for building a Node.js native add-on.
#
# Main documentation:
#
# [1]: https://gyp.gsrc.io/docs/InputFormatReference.md
# [2]: https://gyp.gsrc.io/docs/UserDocumentation.md
{
  # Define variables to be used throughout the configuration for all targets:
  'variables': {
    # Source directory:
    'src_dir': './src',

    # Include directories:
    'include_dirs': [
      '<!@(node -e "var arr = require(\'@stdlib/utils/library-manifest\')(\'./manifest.json\',{},{\'basedir\':process.cwd(),\'paths\':\'posix\'}).include; for ( var i = 0; i < arr.length; i++ ) { console.log( arr[ i ] ); }")',
    ],

    # Add-on destination directory:
    'addon_output_dir': './src',

    # Source files:
    'src_files': [
      '<(src_dir)/addon.c',
      '<!@(node -e "var arr = require(\'@stdlib/utils/library-manifest\')(\'./manifest.json\',{},{\'basedir\':process.cwd(),\'paths\':\'posix\'}).src; for ( var i = 0; i < arr.length; i++ ) { console.log( arr[ i ] ); }")',
    ],

    # Library dependencies:
    'libraries': [
      '<!@(node -e "var arr = require(\'@stdlib/utils/library-manifest\')(\'./manifest.json\',{},{\'basedir\':process.cwd(),\'paths\':\'posix\'}).libraries; for ( var i = 0; i < arr.length; i++ ) { console.log( arr[ i ] ); }")',
    ],

    # Library directories:
    'library_dirs': [
      '<!@(node -e "var arr = require(\'@stdlib/utils/library-manifest\')(\'./manifest.json\',{},{\'basedir\':process.cwd(),\'paths\':\'posix\'}).libpath; for ( var i = 0; i < arr.length; i++ ) { console.log( arr[ i ] ); }")',
    ],
  }, # end variables
}
