module.exports = function(grunt) {
  grunt.loadNpmTasks("grunt-ts");

  grunt.initConfig({
    ts: {
      main: {
        src: ["UdemyCourse/Tryouts/src/*.ts"],
        out: "UdemyCourse/Tryouts/bin/final.js"
        //dest: "UdemyCourse/Tryouts/bin"
      }
    }
  });

  grunt.registerTask("default", ["ts"]);
};
