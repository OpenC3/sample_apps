class CreateCompanies < ActiveRecord::Migration[8.0]
  def change
    create_table :companies do |t|
      t.string :name
      t.boolean :customer

      t.timestamps
    end
  end
end
