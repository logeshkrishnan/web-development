-- =======================================================
-- Create Stored Procedure Template for Azure SQL Database
-- =======================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:      <Author, , Name>
-- Create Date: <Create Date, , >
-- Description: <Description, , >
-- =============================================
CREATE PROCEDURE dbo.InsertMasterData
(
    -- Add the parameters for the stored procedure here
    @material_of_construction varchar(MAX)
	@moulding_process varchar(MAX)
	@neck_type varchar(MAX)
	@sku varchar(10)
	@product varchar(MAX)
	@best_suited_for varchar(MAX)
	@container_type varchar(30)
	@vendor_name varchar(MAX)
	@product_name varchar(MAX)
	@ofc varchar(MAX)
	@weight varchar(10)
	@price varchar(10)
	@shape varchar(30)
)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON

    -- Insert statements for procedure here
    SELECT <@Param1, sysname, @p1>, <@Param2, sysname, @p2>
END
GO
