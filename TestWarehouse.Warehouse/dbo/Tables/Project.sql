CREATE TABLE [dbo].[Project] (

	[project_id] int NULL, 
	[project_name] varchar(8000) NULL, 
	[project_code] varchar(8000) NULL, 
	[details] varchar(8000) NULL, 
	[is_active] bit NULL, 
	[created_at] varchar(8000) NULL, 
	[last_modified] varchar(8000) NULL, 
	[created_by_id] int NULL, 
	[delivery_unit_id] int NULL, 
	[group_id] bigint NULL, 
	[last_modified_by_id] int NULL, 
	[is_measurable] bit NULL
);

