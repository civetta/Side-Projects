# Define Functions -------------------------------------------------------------
ConnectToDB_IM <- function() {
  # Connect to the Imagine Math data warehouse
  #
  # Returns:
  #   A database connection

  dbConnect(
    drv =
      JDBC(
        driverClass = "com.amazon.redshift.jdbc42.Driver",
        identifier.quote = "`",
        classPath = "~/R/RedshiftJDBC42-no-awssdk-CURRENT.jar"
      ),
    url =
      with(
        config::get("datawarehouse", file = "~/R/config.yml"),
        paste0(
          "jdbc:redshift://", server, ":", port, "/", database, "?user=", uid,
          "&password=",rawToChar(base64enc::base64decode(pwd)))
      )
  )
}

testing <- ConnectToDB_IM()
